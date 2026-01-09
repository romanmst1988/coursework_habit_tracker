from rest_framework import serializers

from habits.models import Habit
from habits.validators import habit_validator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, attrs):
        habit_validator(attrs)
        return attrs
