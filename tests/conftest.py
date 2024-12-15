# tests/conftest.py
import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import Settings
from app.core.sql_models import Base
from app.core.engine import db_helper

# Используем SQLite в памяти для тестов
DATABASE_URL = "sqlite+aiosqlite:///:memory:"

# Создаем асинхронный движок и сессию
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

@pytest.fixture(scope="function")
async def session() -> AsyncSession:
    # Создаем таблицы для теста
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Создаем сессию для каждого теста
    async_session = AsyncSessionLocal()
    try:
        yield async_session
    finally:
        # После каждого теста очищаем базу
        await async_session.close()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
