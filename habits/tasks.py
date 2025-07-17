"""
Отложенные и периодические задачи приложения `habits`.
Для запуска задач необходимо параллельно в
разных окнах терминал запустить команды:
1. Celery-Worker: >> `celery -A config worker -l INFO` + (-P eventlet, для Windows)
2. Celery-Beat: >> `celery -A config beat -l INFO`

"""

from datetime import timedelta
from django.conf import settings

from django.utils import timezone
from celery import shared_task
from pytz import timezone as pytz_timezone

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def check_and_send_habit_reminders():
    """
    Проверяет привычки, которым нужно отправить напоминание
    """
    now = timezone.now()
    habits_to_remind = Habit.objects.filter(
        time__gte=now, time__lt=now + timedelta(hours=1), user__tg_chat_id__isnull=False
    )

    for habit in habits_to_remind:
        print(f"Habit time: {habit.time}, Now: {now}")
        if should_send_reminder(habit, now):
            send_habit_reminder.delay(habit.id)


def should_send_reminder(habit, current_time):
    """
    Проверяет, нужно ли отправлять напоминание для привычки
    """
    if habit.last_completed is None:
        return True
    last = habit.last_completed
    now = current_time
    if habit.periodicity == 1:
        return last.date() != now.date()
    elif habit.periodicity == 2:
        return (now - last).days >= 2
    elif habit.periodicity == 7:
        return (now - last).days >= 7
    return False


@shared_task
def send_habit_reminder(habit_id):
    """
    Отправляет напоминание о привычке
    """
    habit = Habit.objects.get(id=habit_id)
    chat_id = habit.user.tg_chat_id
    if chat_id:
        moscow_tz = pytz_timezone(settings.TIME_ZONE)
        local_time = habit.time.astimezone(moscow_tz)
        message = (
            f"Напоминание о привычке:\n"
            f"Действие: {habit.action}\n"
            f"Место: {habit.place or 'не указано'}\n"
            f"Время: {local_time.strftime('%H:%M')}\n"
            f"Периодичность: {habit.get_periodicity_display()}\n"
            f"Вознаграждение: {habit.reward or 'нет'}"
        )
        print(
            "Отправляем сообщение..."
        )  # Для проверки, доходит ли выполнение до этой строки
        send_telegram_message(chat_id=chat_id, message=message)
        habit.last_completed = timezone.now()
        habit.save()
