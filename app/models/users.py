import uuid
from typing import Optional

from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from starlette.requests import Request

from app.core.config import settings
from app.db.base_class import Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID


class User(SQLAlchemyBaseUserTableUUID, Base):
    username = Column(String, nullable=True)

    posts = relationship('Post', back_populates='creator')


class AccessSessionID(SQLAlchemyBaseAccessTokenTableUUID, Base):
    pass


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.SECRET
    verification_token_secret = settings.SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")



