# Mail_Service-TG_Notifications

### Сервис рассылки Email и Telegram-уведомлений 

---

## 🚀 Описание проекта 

Этот проект — универсальный мини-сервис, который позволяет создавать, запускать и контролировать массовые рассылки уведомлений по Email и через Telegram.  
Вся логика реализована на FastAPI, задачи отправки выполняются через Celery с брокером Redis. Данные пользователей, кампаний и статистики хранятся в PostgreSQL.

**Особенности:**
- REST API для управления пользователями, кампаниями, задачами рассылки
- Асинхронная работа (FastAPI + SQLAlchemy + asyncpg)
- Отправка уведомлений через email и Telegram (можно подключать другие каналы)
- Очереди задач через Celery + Redis (масштабирование, высокая скорость обработки)
- Удобная архитектура для расширения
- Готов к запуску в Docker-окружении

---

## 📂 Структура проекта

- **app/api/** — роутеры FastAPI
- **app/db/** — работа с базой данных и сессиями
- **app/models/** — SQLAlchemy-модели
- **app/schemas/** — Pydantic-схемы (валидация данных)
- **app/tasks/** — задачи Celery
- **app/utils/** — утилиты, эмуляторы отправки
- **celery_app.py** — инициализация Celery
- **config.py** — настройки проекта
- **main.py** — главная точка входа FastAPI
- **.env** — переменные окружения
- **requirements.txt** — зависимости Python
- **docker-compose.yml** — настройка сервисов для Docker Compose
- **Dockerfile** — сборка Docker-образа
- **README.md** — описание и инструкция


## ⚡ Быстрый старт (Windows, без Docker)

### 1. Установи Python 3.11+  
[Скачать Python для Windows](https://www.python.org/downloads/windows/)

### 2. 
git clone https://github.com/Jeff555max/Mail_Service-TG_Notifications.git

cd Mail_Service-TG_Notifications

3. Создай и активируй виртуальное окружение

python -m venv .venv

.venv\Scripts\activate

4. Установи зависимости

pip install --upgrade pip

pip install -r requirements.txt

5. Настрой файл .env

Пример содержимого для локального запуска:


DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/postgres

REDIS_BROKER_URL=redis://localhost:6379/0

Убедись, что PostgreSQL и Redis запущены на твоей машине!

6. Запусти Redis
(скачай redis для Windows, распакуй и запусти redis-server.exe)

7. Запусти FastAPI

uvicorn app.main:app --reload

Swagger UI будет доступен по адресу: http://127.0.0.1:8000/docs

8. Запусти Celery worker

celery -A app.celery_app.celery worker --loglevel=info --pool=solo



## 🐳 Запуск через Docker Compose (Linux/macOS/WSL/Windows с Docker Desktop)

docker compose up --build

Это поднимет сервис FastAPI, Celery worker, Redis и PostgreSQL в контейнерах.

В файле docker-compose.yml введите свои данные для подключения к базе данных и Redis.

Настрой файл .env

Пример содержимого для  запуска:

REDIS_BROKER_URL=redis://redis:6379/0

DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/postgres


Swagger UI: http://localhost:8000/docs


📑 Пример запроса для рассылки через API

POST /api/campaigns/

1.

{

  "title": "Информирование клиентов",

  "text": "Скидки на все цветы только сегодня!",

  "users": [

    {"email": "user1@mail.com", "telegram_id": "12345"},

    {"email": "user2@mail.com"}

  ]

}
2.

Пример тела запроса (JSON)

Нужно указать текст рассылки и список ID пользователей (user_ids), которым отправится уведомление. 
Пример:


{
  "text": "Всем привет! Это тестовая рассылка.",
  "user_ids": [1, 2, 3]
}

Ответ:

 curl -X 'POST' \
  'http://localhost:8000/campaigns/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Всем привет! Это тестовая рассылка.",
  "user_ids": [1, 2, 3]
}
'







