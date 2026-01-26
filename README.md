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

## 🚀 Запуск проекта через Docker Compose

- В этом разделе описано, как быстро поднять проект с помощью Docker Compose.

## 📌 Требования

- Перед началом убедись, что на твоей машине установлены:

1. Docker Engine

2. Docker Compose (может быть встроен в Docker CLI как docker compose)

## 🧱 Как запустить проект

- Клонируй репозиторий и перейди в корень проекта

- git clone https://github.com/romanmst1988/coursework_habit_tracker.git
- cd coursework_habit_tracker


- Создай (или обнови) файл .env при необходимости (если проект использует переменные окружения).

- Запусти контейнеры

- docker compose up -d --build


- Эта команда построит образы (если это необходимо) и запустит все сервисы в фоне.

- Посмотреть статус запущенных сервисов

- docker compose ps


- Остановить контейнеры

- docker compose down

## 🔍 Проверка работоспособности сервисов

- После запуска убедись, что все сервисы работают корректно:

## 🧪 1. Основной сервис (API + UI)

- Открой в браузере:

- http://localhost:8000


- (или указанный в docker-compose.yml порт)

- Ты должен увидеть стартовую страницу или API-ответ приложения.

## 🧪 2. База данных

- Если у тебя в docker-compose.yml есть, например, PostgreSQL (или другая БД), проверь, что контейнер поднят и доступен:

- docker compose logs db


- Здесь будут логи контейнера базы данных.

## 🧪 3. Логи всех сервисов

- Чтобы посмотреть логи всех контейнеров:

- docker compose logs -f


- Если какой-то сервис упал, в логах ты сразу увидишь ошибку.

## 📌 Полезные команды Docker Compose
- Команда	Описание
- docker compose up	Запустить контейнеры
- docker compose up -d	Запустить в фоне
- docker compose down	Остановить и удалить контейнеры
- docker compose ps	Показать статус
- docker compose logs	Показать логи
# 📝 Примечания

- После первого запуска образы могут занять некоторое время на сборку.

- Если что-то не стартует — проверь переменные окружения и порты, указанные в docker-compose.yml.

## Docker Compose

### Сервисы проекта

- web — Django REST API
- db — PostgreSQL
- redis — брокер сообщений Celery
- celery — обработчик фоновых задач
- celery-beat — планировщик периодических задач

### Запуск проекта

```bash
docker compose up --build