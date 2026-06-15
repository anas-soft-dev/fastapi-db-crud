from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserSchema
from app.models.user import User
from app.models.post import Post
from app.database import SessionLocal
from app.dependencies import get_db
from sqlalchemy import or_, and_
from sqlalchemy.orm import selectinload


router = APIRouter(prefix="/user")



@router.get("/post")
def all_user_post(db = Depends(get_db)):
    users = db.query(User).options(selectinload(User.posts)).first()

    return users
@router.get("/post/{user_id}")
def view_user_post(user_id: int, db = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.posts

@router.post("/post/{user_id}")
def save_user_post(user_id: int,data: UserSchema, db = Depends(get_db)):
    user = db.get(User, user_id)
    post = Post(
        title="hello",
        description = "test",
    )
    user.posts.append(post)
    
    # db.add(post)
    db.commit()
    db.refresh(post)
    return post


@router.get("")
def view(db = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/search")
def search(name:str = "",db = Depends(get_db)):
    users = db.query(User).filter(User.name.contains(name)).all()
    
    # users = db.query(User).filter(
    #     or_(
    #         User.name.ilike(f"%{name}%"),
    #         User.email.endswith("gmail.com")
    #     )
    #     ).all()
    return users

@router.post("")
def store(request: UserSchema, db = Depends(get_db)):

    user = User(
       name = request.name,
       email = request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

@router.put("/{user_id}")
def update(user_id: int, data: UserSchema, db = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    existing_user = db.query(User).filter(
            User.email == data.email
        ).first()

    if not user:
        raise HTTPException(status_code=404,detail="User does not exist")
    
    if existing_user:
        raise HTTPException(status_code=422,detail="Email already exists")

    
    user.name = data.name
    user.email = data.email

    db.commit()
    db.refresh(user)

    return user


@router.delete("/{user_id}")
def delete(user_id:int, database = Depends(get_db)):
    user =  database.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User does not exist")
    
    database.delete(user)
    database.commit()
    return "deleted"

