from db import engine
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Identity
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__: str = "users"

    id: Mapped[int] = Column(Integer, Identity(always=True), primary_key=True, index=True)
    email: Mapped[str] = Column(String, unique=True, nullable=False)

class UpVotes(Base):
    __tablename__: str = "upvotes"

    id: Mapped[int] = Column(Integer, Identity(always=True), primary_key=True, index=True)
    sid: Mapped[str] = Column(Text, unique=True, nullable=False)
