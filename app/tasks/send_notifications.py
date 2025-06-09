from app.utils.celery_app import celery

@celery.task
def send_notification(to, subject, body):
    # Твоя логика отправки (email/telegram и т.д.)
    print(f"Sending notification to {to}: {subject} — {body}")
    return True
