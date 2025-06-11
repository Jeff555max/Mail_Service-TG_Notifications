from dotenv import load_dotenv
load_dotenv()

import os
from celery import Celery

print("REDIS_BROKER_URL:", os.environ.get("REDIS_BROKER_URL"))  # Для отладки

CELERY_BROKER_URL = os.environ.get("REDIS_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("REDIS_BROKER_URL")

celery = Celery(
    "app",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=["app.tasks.send_notifications"]
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Europe/Moscow",
    enable_utc=True,
)
