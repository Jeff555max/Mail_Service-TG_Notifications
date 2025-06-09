from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey
from app.db.session import Base
from datetime import datetime
import enum

class StatusEnum(enum.Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    telegram_id = Column(String, nullable=True)

class Campaign(Base):
    __tablename__ = "campaigns"
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class CampaignUser(Base):
    __tablename__ = "campaign_users"
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.pending)
