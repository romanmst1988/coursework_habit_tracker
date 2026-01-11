from celery import shared_task

from habits.models import Habit
from telegram_bot.services import send_telegram_message


@shared_task
def send_habit_reminders():
    habits = Habit.objects.filter(is_public=False)

    for habit in habits:
        if hasattr(habit.user, "telegram"):
            message = (
                f"⏰ Напоминание!\n"
                f"Действие: {habit.action}\n"
                f"Место: {habit.place}\n"
                f"Время: {habit.time}"
            )
            send_telegram_message(habit.user.telegram.chat_id, message)
