from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import User
from app.db.session import get_async_session
from app.schemas.schemas import UserCreate, UserRead

router = APIRouter(prefix="/users")

@router.get("/", response_model=list[UserRead])
async def get_users(db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(select(User))
    return result.scalars().all()

@router.post("/", response_model=UserRead)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_async_session)):
    db_user = User(email=user.email, telegram_id=user.telegram_id)
    db.add(db_user)
    try:
        await db.commit()
        await db.refresh(db_user)
        return db_user
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
