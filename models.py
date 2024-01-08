from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel):
    id: int
    email: str

class UpVote(SQLModel):
    id: int
    sid: str = Field(nullable=False)
