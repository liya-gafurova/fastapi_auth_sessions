from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy import String, Column, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Post(Base):
    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    text = Column(Text)
    created = Column(DateTime(timezone=True))

    creator_id = Column(GUID, ForeignKey('user.id'))

    creator = relationship('User', back_populates='posts')
