from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserSchema
from app.models.user import User
from app.database import SessionLocal
from app.dependencies import get_db
from sqlalchemy import or_, and_


router = APIRouter(prefix="/user")


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
def delete(user_id:int, db = Depends(get_db)):
    user =  db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User does not exist")
    
    db.delete(user)
    db.commit()
    return "deleted"

