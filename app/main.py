from fastapi import FastAPI
from app.db.init_db import init_db

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

# Импортируй и подключи роутеры
from app.api.users import router as users_router
from app.api.campaigns import router as campaigns_router

app.include_router(users_router)
app.include_router(campaigns_router)
