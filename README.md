# Mail_Service-TG_Notifications

### Сервис рассылки Email и Telegram-уведомлений для бизнеса и команд

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
- Готов к запуску в Docker-окружении, поддержка Windows (dev-режим)

---

## 📂 Структура проекта

Mail_Service-TG_Notifications/
├── app/                  # Основное приложение
│   ├── api/              # Роутеры FastAPI
│   ├── db/               # Работа с БД
│   ├── models/           # SQLAlchemy-модели
│   ├── schemas/          # Pydantic-схемы
│   ├── tasks/            # Celery задачи
│   ├── utils/            # Утилиты и эмуляторы
│   ├── __init__.py
│   ├── celery_app.py     # Инициализация Celery
│   ├── config.py         # Настройки
│   └── main.py           # Главная точка входа FastAPI
├── .env                  # Переменные окружения
├── requirements.txt      # Зависимости
├── docker-compose.yml    # Docker Compose
├── Dockerfile            # Dockerfile
├── README.md             # Описание проекта


## ⚡ Быстрый старт (Windows, без Docker)

### 1. Установи Python 3.11+  
[Скачать Python для Windows](https://www.python.org/downloads/windows/)

### 2. Клонируй репозиторий
```sh
git clone https://github.com/Jeff555max/Mail_Service-TG_Notifications.git
cd Mail_Service-TG_Notifications
3. Создай и активируй виртуальное окружение
sh
Копировать
Редактировать
python -m venv .venv
.venv\Scripts\activate
4. Установи зависимости
sh
Копировать
Редактировать
pip install --upgrade pip
pip install -r requirements.txt
5. Настрой файл .env
Пример содержимого для локального запуска:

ini
Копировать
Редактировать
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/postgres
REDIS_BROKER_URL=redis://localhost:6379/0
Убедись, что PostgreSQL и Redis запущены на твоей машине!

6. Запусти Redis
(скачай redis для Windows, распакуй и запусти redis-server.exe)

7. Запусти FastAPI
sh
Копировать
Редактировать
uvicorn app.main:app --reload
Swagger UI будет доступен по адресу: http://127.0.0.1:8000/docs

8. Запусти Celery worker
sh
Копировать
Редактировать
celery -A app.celery_app.celery worker --loglevel=info --pool=solo
Для production-режима или на Linux можно использовать другой pool (gevent/prefork).

🐳 Запуск через Docker Compose (Linux/macOS/WSL/Windows с Docker Desktop)
Важно: Docker должен быть установлен и работать!

sh
Копировать
Редактировать
docker compose up --build
Это поднимет сервис FastAPI, Celery worker, Redis и PostgreSQL в контейнерах.

Swagger UI: http://localhost:8000/docs

🛠️ Команды для разработчика
Форматирование кода:
black app/

Проверка стиля:
flake8 app/

Тесты (если появятся):
pytest

📑 Пример запроса для рассылки через API
json
Копировать
Редактировать
POST /api/campaigns/
{
  "title": "Информирование клиентов",
  "text": "Скидки на все цветы только сегодня!",
  "users": [
    {"email": "user1@mail.com", "telegram_id": "12345"},
    {"email": "user2@mail.com"}
  ]
}
🏆 Авторы и поддержка
Евгений Богачев
Telegram: @JJJeFFF5
GitHub: Jeff555max

⚠️ Важно
На Windows запуск Docker/Redis/Postgres может требовать прав администратора!

На Windows Celery работайте с пулом --pool=solo для отладки.

Для production и стабильной работы рекомендуем запускать всё через Docker/на Linux.





