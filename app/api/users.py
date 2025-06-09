from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import User
from app.db.session import get_async_session

router = APIRouter(prefix="/users")

@router.get("/")
async def get_users(db: AsyncSession = Depends(get_async_session)):
    result = await db.execute("SELECT * FROM users;")
    return result.fetchall()
