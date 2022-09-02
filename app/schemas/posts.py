from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from pydantic.schema import datetime, date


class PostCreate(BaseModel):
    title: str
    text: str


class PostDB(PostCreate):
    created: date
    id: str
    creator_id: UUID

    class Config:
        orm_mode = True


class PostUpdate(BaseModel):
    title: Optional[str]
    text: Optional[str]


class PostRead(PostCreate):
    id: str
    title: str
    text: str
    created: datetime

    class Config:
        orm_mode = True
