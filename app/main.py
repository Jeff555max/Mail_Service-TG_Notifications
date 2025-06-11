from dotenv import load_dotenv
load_dotenv()  # ← Самое первое!

import os
print("DATABASE_URL:", os.environ.get("DATABASE_URL"))
print("REDIS_BROKER_URL:", os.environ.get("REDIS_BROKER_URL"))

from fastapi import FastAPI

# Только теперь импортируем то, что использует переменные!
from app.db.init_db import init_db
from app.api.users import router as users_router
from app.api.campaigns import router as campaigns_router

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(users_router)
app.include_router(campaigns_router)
