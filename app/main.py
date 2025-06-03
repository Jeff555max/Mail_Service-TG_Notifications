from fastapi import FastAPI
from app.db.init_db import init_db
from app.api.users import router as users_router
from app.api.campaigns import router as campaigns_router
app = FastAPI()

init_db() # Вызов инициализации базы данных


app = FastAPI(
    title="Email & Telegram Campaign Service"
)

app.include_router(users_router)
app.include_router(campaigns_router)
