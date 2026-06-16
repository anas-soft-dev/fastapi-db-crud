from fastapi import APIRouter, Depends, HTTPException
from app.schemas.post import PostSchema
from app.models.post import Post
from app.dependencies import get_db
from sqlalchemy.orm import selectinload


router = APIRouter(prefix="/post",tags=["Post"])



@router.post("")
def save(data:PostSchema ,db = Depends(get_db)):
   # category =  Post(title=data.title, description=data.desciption,user_id=data.user_id,category_id=data.category_id)
   post =  Post(**data.model_dump())

   db.add(post)
   db.commit()
   db.refresh(post)

   return post

@router.get("")
def view(category_id:int = None, title:str = None ,db = Depends(get_db)):
   query = db.query(Post)

   if category_id:
      query = query.filter(Post.category_id == category_id)
   
   if title:
      query = query.filter(Post.title.contains(title))

   posts = query.all()

   return posts