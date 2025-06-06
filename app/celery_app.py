import os
from celery import Celery

CELERY_BROKER_URL = os.getenv("REDIS_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv("REDIS_BROKER_URL", "redis://localhost:6379/0")

celery = Celery(
    "mail_service",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)
celery.conf.task_routes = {
    "app.tasks.send_notifications.send_campaign": {"queue": "mail_queue"},
}
