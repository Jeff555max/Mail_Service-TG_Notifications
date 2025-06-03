from fastapi import FastAPI
from app.db.init_db import init_db

app = FastAPI()

init_db() # Вызов инициализации базы данных
