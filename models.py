from sqlmodel import SQLModel
from typing import Optional

class User(SQLModel):
    id: int
    email: str

class UpVote(SQLModel):
    id: int
    uuid: str
