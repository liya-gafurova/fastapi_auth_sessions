from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate


class UserDB(BaseUser):
    pass


class UserCreate(BaseUserCreate):
    pass


class UserUpdate(BaseUserUpdate):
    pass

