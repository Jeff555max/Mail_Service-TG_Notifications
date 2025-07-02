from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.db.models import User, Campaign, CampaignUser, StatusEnum

async def create_user(db: AsyncSession, email: str, telegram_id: str = None):
    user = User(email=email, telegram_id=telegram_id)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

async def create_campaign(db: AsyncSession, text: str, user_ids: list[int]):
    campaign = Campaign(text=text)
    db.add(campaign)
    await db.commit()
    await db.refresh(campaign)
    # Привязываем пользователей к кампании
    for user_id in user_ids:
        db.add(CampaignUser(campaign_id=campaign.id, user_id=user_id, status=StatusEnum.pending))
    await db.commit()
    return campaign

async def get_campaign(db: AsyncSession, campaign_id: int):
    result = await db.execute(
        select(Campaign).options(selectinload(Campaign.users)).where(Campaign.id == campaign_id)
    )
    return result.scalar_one_or_none()

async def get_campaign_statuses(db: AsyncSession, campaign_id: int):
    result = await db.execute(
        select(CampaignUser, User)
        .join(User, CampaignUser.user_id == User.id)
        .where(CampaignUser.campaign_id == campaign_id)
    )
    return result.all()
