import os

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DSN: str = f"postgresql+asyncpg://{ os.environ['POSTGRES_USER'] }:{ os.environ['POSTGRES_PASSWORD'] }@{ os.environ['POSTGRES_HOST'] }:{ os.environ['POSTGRES_PORT'] }/{ os.environ['POSTGRES_DB'] }"

engine = AsyncEngine(create_engine(DSN, echo=True, future=True))

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session():
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        yield session
