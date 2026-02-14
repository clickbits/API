from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import sqlalchemy as SA

import db
import models

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def getUsers(session: db.AsyncSession = Depends(db.get_session)):
    users: SA.Result = await session.execute(SA.text("SELECT * FROM users"))
    return users.scalars().all()

app.mount("/static", StaticFiles(directory="static"), name="static")
