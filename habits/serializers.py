from rest_framework import serializers

from habits.models import Habit
from habits.validators import habit_validator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        extra_kwargs = {
            "place": {"help_text": "Место выполнения привычки"},
            "action": {"help_text": "Действие"},
            "execution_time": {"help_text": "Время выполнения (HH:MM)"},
            "duration": {"help_text": "Время выполнения в секундах (≤120)"},
            "is_pleasant": {"help_text": "Признак приятной привычки"},
            "related_habit": {"help_text": "Связанная приятная привычка"},
            "reward": {"help_text": "Вознаграждение"},
            "periodicity": {"help_text": "Периодичность в днях (1–7)"},
            "is_public": {"help_text": "Публичная привычка"},
        }
        read_only_fields = ("user",)

    def validate(self, attrs):
        habit_validator(attrs)
        return attrs
