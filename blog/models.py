from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from core.db import Base
from user.models import User


class Post(Base):
    __tablename__ = "blog_post"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String)
    text = Column(String(length=350))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship(User)