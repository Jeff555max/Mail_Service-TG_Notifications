# Инициализация базы данных
from app.db.session import engine, Base
from app.models import models


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
