from fastapi import APIRouter, Depends, HTTPException
from app.schemas.category import CategorySchema
from app.models.category import Category
from app.dependencies import get_db
from sqlalchemy.orm import selectinload


router = APIRouter(prefix="/category",tags=["Category"])



@router.post("")
def save(data:CategorySchema ,db = Depends(get_db)):
   category =  Category(**data.model_dump())

   db.add(category)
   db.commit()
   db.refresh(category)

   return category

@router.get("/post/{category_id}")
def get_post(category_id:int, db = Depends(get_db)):
   category = db.get(Category,category_id)

   return category.posts