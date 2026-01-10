from django.conf import settings
from django.db import models

class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='habits'
    )
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)

    is_pleasant = models.BooleanField(default=False)

    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    reward = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    periodicity = models.PositiveSmallIntegerField(default=1)
    execution_time = models.PositiveSmallIntegerField(
        verbose_name="Время выполнения (сек)",
    )
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.action
