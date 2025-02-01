
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base

# Project directories
from config import global_settings

DBBaseModel = declarative_base()

engine: AsyncEngine = create_async_engine(global_settings.DB_URL)

# Session factory for async session
Session: AsyncSession = sessionmaker(
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)