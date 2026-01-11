from rest_framework.exceptions import ValidationError


def habit_validator(data):
    """
    Валидаторы привычек по ТЗ курсовой
    """

    reward = data.get("reward")
    related_habit = data.get("related_habit")
    is_pleasant = data.get("is_pleasant")
    execution_time = data.get("execution_time")
    periodicity = data.get("periodicity")

    # 1. Нельзя одновременно reward и related_habit
    if reward and related_habit:
        raise ValidationError(
            "Нельзя указывать одновременно вознаграждение и связанную привычку"
        )

    # 2. Время выполнения <= 120 секунд
    if execution_time and execution_time > 120:
        raise ValidationError("Время выполнения не может превышать 120 секунд")

    # 3. Периодичность не реже 1 раза в 7 дней
    if periodicity and periodicity > 7:
        raise ValidationError("Нельзя выполнять привычку реже 1 раза в 7 дней")

    # 4. У приятной привычки не может быть reward и related_habit
    if is_pleasant and (reward or related_habit):
        raise ValidationError(
            "У приятной привычки не может быть вознаграждения или связанной привычки"
        )

    # 5. Связанная привычка должна быть приятной
    if related_habit and not related_habit.is_pleasant:
        raise ValidationError("Связанная привычка должна быть приятной")
