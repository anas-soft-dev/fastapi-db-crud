from fastapi import FastAPI
from app.routers.user import router as user_router
from app.database import Base, engine

app = FastAPI()

app.include_router(user_router)

Base.metadata.create_all(engine)
