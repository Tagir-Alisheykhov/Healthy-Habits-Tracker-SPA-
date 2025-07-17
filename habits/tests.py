from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from pytz import timezone as pytz_timezone
from accounts.models import User
from habits.models import Habit
from habits.tasks import check_and_send_habit_reminders, should_send_reminder, send_habit_reminder
from unittest.mock import patch


class HabitTasksTestCase(TestCase):
    def setUp(self):
        # Создаем пользователя с учетом всех обязательных полей
        self.user = User.objects.create(
            email='test@example.com',
            password='testpass123',
            username='testuser',
            tg_chat_id='123456',  # обязателен для отправки напоминаний
            phone='+79991234567'
        )

        # Текущее время (с учётом таймзоны)
        moscow_tz = pytz_timezone('Europe/Moscow')
        now = timezone.now().astimezone(moscow_tz)

        # Привычка должна срабатывать через 30 минут от текущего времени
        self.habit = Habit.objects.create(
            user=self.user,
            action="Пить воду",
            time=now + timedelta(minutes=30),  # чтобы точно попало в окно [now, now+1h]
            execution_time=30,
            periodicity=1,
            last_completed=now - timedelta(days=1)  # была выполнена вчера
        )

    def test_should_send_reminder(self):
        """Тестируем логику определения необходимости напоминания"""
        now = timezone.now()

        # Привычка не выполнена сегодня — должно отправиться
        self.assertTrue(should_send_reminder(self.habit, now))

        # Выполняем привычку сегодня
        self.habit.last_completed = now
        self.habit.save()
        self.assertFalse(should_send_reminder(self.habit, now))

    @patch('habits.tasks.send_telegram_message')
    def test_send_habit_reminder(self, mock_send):
        """Тестируем отправку напоминания"""
        send_habit_reminder(self.habit.id)

        # Проверяем, что сообщение было отправлено
        mock_send.assert_called_once()

        # Проверяем обновление времени последнего выполнения
        updated_habit = Habit.objects.get(id=self.habit.id)
        self.assertAlmostEqual(
            updated_habit.last_completed,
            timezone.now(),
            delta=timedelta(seconds=5)
        )

    @patch('habits.tasks.send_habit_reminder.delay')
    def test_check_and_send_habit_reminders(self, mock_delay):
        """Тестируем основную задачу проверки привычек"""
        check_and_send_habit_reminders()

        # Проверяем, что задача на отправку была вызвана с правильным id
        mock_delay.assert_called_once_with(self.habit.id)

    def test_timezone_conversion(self):
        """Тестируем корректность конвертации времени"""
        moscow_tz = pytz_timezone('Europe/Moscow')
        local_time = self.habit.time.astimezone(moscow_tz)

        # Проверяем, что время корректно конвертируется
        self.assertEqual(local_time.tzinfo.zone, 'Europe/Moscow')
