from app.celery_app import celery
from app.utils.notification import send_email, send_telegram
from app.db.session import SessionLocal
from app.db.models import CampaignUser, User, StatusEnum

@celery.task
def send_campaign(campaign_id):
    """
    Celery-задача: отправить уведомления по кампании, обновить статусы в БД.
    """
    db = SessionLocal()
    try:
        # Получаем всех пользователей, которым нужно отправить
        users = db.query(CampaignUser).filter(CampaignUser.campaign_id == campaign_id).all()
        for campaign_user in users:
            user = db.query(User).get(campaign_user.user_id)
            try:
                # Пробуем отправить email
                if user.email:
                    send_email(user.email, f"Рассылка №{campaign_id}", "Вам сообщение!")
                # Пробуем отправить Telegram
                if user.telegram_id:
                    send_telegram(user.telegram_id, "Вам сообщение!")
                # Если всё ок — обновляем статус
                campaign_user.status = StatusEnum.sent
                print(f"Уведомление отправлено пользователю {user.email or user.telegram_id}")
            except Exception as e:
                # Если была ошибка — статус failed
                campaign_user.status = StatusEnum.failed
                print(f"Ошибка отправки пользователю {user.email or user.telegram_id}: {e}")
        db.commit()
    except Exception as e:
        print(f"Ошибка выполнения рассылки {campaign_id}: {e}")
    finally:
        db.close()
