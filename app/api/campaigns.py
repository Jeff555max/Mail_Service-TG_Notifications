from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.schemas import CampaignCreate, CampaignRead, CampaignStatusList, CampaignStatus
from app.db.crud import create_campaign, get_campaign, get_campaign_statuses
from app.db.session import get_async_session

router = APIRouter(prefix="/campaigns", tags=["campaigns"])

@router.post("/", response_model=CampaignRead, status_code=status.HTTP_201_CREATED)
async def create_campaign_view(data: CampaignCreate, db: AsyncSession = Depends(get_async_session)):
    campaign = await create_campaign(db, text=data.text, user_ids=data.user_ids)
    # Здесь можно запланировать асинхронную задачу через Celery
    return campaign

@router.get("/{campaign_id}/status", response_model=CampaignStatusList)
async def get_campaign_status_view(campaign_id: int, db: AsyncSession = Depends(get_async_session)):
    rows = await get_campaign_statuses(db, campaign_id=campaign_id)
    statuses = [
        CampaignStatus(
            user_id=u.id,
            status=c.status,
            email=u.email,
            telegram_id=u.telegram_id
        ) for c, u in rows
    ]
    return CampaignStatusList(campaign_id=campaign_id, statuses=statuses)
