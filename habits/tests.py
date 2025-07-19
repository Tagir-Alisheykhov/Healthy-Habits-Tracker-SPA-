from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from pytz import timezone as pytz_timezone
from accounts.models import User
from habits.models import Habit
from habits.tasks import (
    check_and_send_habit_reminders,
    should_send_reminder,
    send_habit_reminder,
)
from unittest.mock import patch


class HabitTasksTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@example.com",
            password="testpass123",
            username="testuser",
            tg_chat_id="123456",
            phone="+79991234567",
        )

        moscow_tz = pytz_timezone("Europe/Moscow")
        now = timezone.now().astimezone(moscow_tz)

        self.habit = Habit.objects.create(
            user=self.user,
            action="Пить воду",
            time=now + timedelta(minutes=30),
            execution_time=30,
            periodicity=1,
            last_completed=now - timedelta(days=1),
        )

    def test_should_send_reminder(self):
        """Тестирование логики определения необходимости напоминания"""
        now = timezone.now()

        # Привычка не выполнена сегодня — должно отправиться
        self.assertTrue(should_send_reminder(self.habit, now))

        # Выполнение привычки сегодня
        self.habit.last_completed = now
        self.habit.save()
        self.assertFalse(should_send_reminder(self.habit, now))

    @patch("habits.tasks.send_telegram_message")
    def test_send_habit_reminder(self, mock_send):
        """Тестирование отправки напоминания"""
        send_habit_reminder(self.habit.id)

        # Проверка, что сообщение было отправлено
        mock_send.assert_called_once()

        # Проверка обновления времени последнего выполнения
        updated_habit = Habit.objects.get(id=self.habit.id)
        self.assertAlmostEqual(
            updated_habit.last_completed, timezone.now(), delta=timedelta(seconds=5)
        )

    @patch("habits.tasks.send_habit_reminder.delay")
    def test_check_and_send_habit_reminders(self, mock_delay):
        """Тестирование основной задачи проверки привычек"""
        check_and_send_habit_reminders()

        # Проверяет, что задача на отправку была вызвана с правильным id
        mock_delay.assert_called_once_with(self.habit.id)

    def test_timezone_conversion(self):
        """Тестирование корректности конвертации времени"""
        moscow_tz = pytz_timezone("Europe/Moscow")
        local_time = self.habit.time.astimezone(moscow_tz)

        # Проверка, что время корректно конвертируется
        self.assertEqual(local_time.tzinfo.zone, "Europe/Moscow")
