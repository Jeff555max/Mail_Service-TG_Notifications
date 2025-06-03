from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.db.session import Base

class StatusEnum(str, enum.Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    telegram_id = Column(String, unique=True, index=True, nullable=True)

    campaigns = relationship("CampaignUser", back_populates="user")

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    users = relationship("CampaignUser", back_populates="campaign")

class CampaignUser(Base):
    __tablename__ = "campaign_users"

    campaign_id = Column(Integer, ForeignKey("campaigns.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.pending)

    campaign = relationship("Campaign", back_populates="users")
    user = relationship("User", back_populates="campaigns")
