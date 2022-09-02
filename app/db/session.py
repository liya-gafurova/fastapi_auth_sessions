from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})
async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False)