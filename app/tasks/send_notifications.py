from app.celery_app import celery
from app.utils.notification import send_email, send_telegram

@celery.task
def send_campaign(campaign_id, user_list, text):
    for user in user_list:
        email = user.get("email")
        telegram_id = user.get("telegram_id")
        try:
            if email:
                send_email(email, text)
            if telegram_id:
                send_telegram(telegram_id, text)
            print(f"Уведомление отправлено пользователю {user}")
        except Exception as e:
            print(f"Ошибка отправки пользователю {user}: {e}")
