from typing import Generator, AsyncGenerator

from fastapi import Depends
from fastapi_users.authentication.strategy import AccessTokenDatabase, DatabaseStrategy
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base_class import Base
from app.db.session import async_session_maker, engine
from app.models import User
from app.models.users import UserManager, AccessSessionID


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(async_session=Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(async_session, User)


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


def get_access_session_id_db(db_session=Depends(get_async_session)):
    return SQLAlchemyAccessTokenDatabase(db_session, AccessSessionID)


def get_database_strategy(
        access_session_id_db: AccessTokenDatabase[AccessSessionID] = Depends(get_access_session_id_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(access_session_id_db, lifetime_seconds=3600)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
