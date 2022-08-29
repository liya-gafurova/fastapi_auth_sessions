from sqlalchemy import String, Column, Text, DateTime, ForeignKey

from app.db.base_class import Base


class Post(Base):
    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    text = Column(Text)
    created = Column(DateTime(timezone=True))