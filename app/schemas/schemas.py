from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum

class StatusEnum(str, Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"

class UserCreate(BaseModel):
    email: EmailStr
    telegram_id: Optional[str] = None

class UserRead(BaseModel):
    id: int
    email: EmailStr
    telegram_id: Optional[str]

    class Config:
        from_attributes = True  # Для pydantic v2 (замена orm_mode = True)

class CampaignCreate(BaseModel):
    text: str
    user_ids: List[int]

class CampaignRead(BaseModel):
    id: int
    text: str
    created_at: datetime

    class Config:
        from_attributes = True

class CampaignStatus(BaseModel):
    user_id: int
    status: StatusEnum
    email: EmailStr
    telegram_id: Optional[str] = None

class CampaignStatusList(BaseModel):
    campaign_id: int
    statuses: List[CampaignStatus]
