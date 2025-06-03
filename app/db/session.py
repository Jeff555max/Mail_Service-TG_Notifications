import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Получаем строку подключения к БД из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")

# Создаем асинхронный движок SQLAlchemy
engine = create_async_engine(DATABASE_URL, future=True, echo=True)

# Создаем фабрику сессий
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Базовый класс для моделей
Base = declarative_base()

# Зависимость FastAPI для получения сессии
async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session
