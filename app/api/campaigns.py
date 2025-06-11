from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.schemas import CampaignCreate, CampaignStatus
from app.db.session import get_async_session
from app.db.models import Campaign, CampaignUser, User, StatusEnum
from app.celery_app import celery
from sqlalchemy import select


router = APIRouter(prefix="/campaigns")

@router.post("/", response_model=CampaignStatus)
async def create_campaign(c: CampaignCreate, db: AsyncSession = Depends(get_async_session)):
    campaign = Campaign(text=c.text)
    db.add(campaign)
    await db.flush()
    # создаем записи для каждого пользователя
    for uid in c.user_ids:
        db.add(CampaignUser(campaign_id=campaign.id, user_id=uid))
    await db.commit()
    # запускаем Celery задачу
    celery.send_task("app.tasks.send_campaign", args=[campaign.id])
    return {"campaign_id": campaign.id, "status": "scheduled"}

@router.get("/{campaign_id}/status", response_model=list[CampaignStatus])
async def get_status(campaign_id: int, db: AsyncSession = Depends(get_async_session)):
    res = await db.execute(
        select(CampaignUser).where(CampaignUser.campaign_id == campaign_id)
    )
    rows = res.scalars().all()
    return [{"user_id": r.user_id, "status": r.status.value} for r in rows]
