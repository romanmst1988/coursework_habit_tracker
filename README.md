# Habit Tracker API

API-сервис для трекинга привычек с напоминаниями в Telegram.  
Реализован на Django + DRF + Celery + Redis.

---

## 🚀 Возможности

- Регистрация и авторизация пользователей (JWT)
- CRUD привычек
- Публичные привычки
- Фильтрация и пагинация
- Отправка напоминаний о привычках в Telegram
- Планировщик напоминаний через Celery Beat
- Документация API через Swagger / OpenAPI

---

## 🧰 Технологии

- Python 3.12
- Django
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- Celery Beat
- JWT (SimpleJWT)
- drf-yasg (Swagger)
- Telegram Bot API

---

## 🚀 Запуск проекта

1. Установите зависимости:
```
pip install -r requirements.txt
```

2. Примените миграции:
```
python manage.py migrate
```

3. Запустите сервер:
```
python manage.py runserver
```

---

## 🔐 Авторизация

- POST /api/users/register/
- POST /api/users/login/
- POST /api/users/token/refresh/

---

## 📑 Документация

Swagger доступен по адресу:
http://127.0.0.1:8000/swagger/
