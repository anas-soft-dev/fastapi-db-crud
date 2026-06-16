from fastapi import FastAPI
from app.models.user import User
from app.models.category import Category
from app.models.post import Post
from app.routers.user import router as user_router
from app.routers.category import router as category_router
from app.routers.post import router as post_router
from app.database import Base, engine

app = FastAPI()

app.include_router(user_router)
app.include_router(post_router)
app.include_router(category_router)

Base.metadata.create_all(engine)
