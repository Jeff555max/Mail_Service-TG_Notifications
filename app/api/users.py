from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.schemas import UserCreate, UserRead
from app.db.crud import create_user, get_user
from app.db.session import get_async_session

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user_view(user: UserCreate, db: AsyncSession = Depends(get_async_session)):
    existing = await get_user(db, user_id=user.email)
    if existing:
        raise HTTPException(status_code=400, detail="User with this email already exists.")
    user_obj = await create_user(db, email=user.email, telegram_id=user.telegram_id)
    return user_obj
