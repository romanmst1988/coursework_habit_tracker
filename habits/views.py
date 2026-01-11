from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from habits.models import Habit
from habits.serializers import HabitSerializer
from habits.permissions import IsOwner
from habits.pagination import HabitPagination

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class PublicHabitViewSet(ReadOnlyModelViewSet):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Список публичных привычек",
        operation_description="""
Возвращает список всех публичных привычек других пользователей.

🔹 Доступно без авторизации  
🔹 Только чтение  
🔹 Используется для экрана «Примеры привычек»
""",
        responses={200: HabitSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Детали публичной привычки",
        operation_description="Просмотр одной публичной привычки",
        responses={200: HabitSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicHabitListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
    pagination_class = HabitPagination
