from pydantic import BaseModel, Field, EmailStr, field_validator
from fastapi import Depends
from app.dependencies import get_db
from app.models.user import User

class UserSchema(BaseModel):
    name:str = Field(min_length=3, max_length=50)
    email:EmailStr
    # @field_validator("email")
    # @classmethod
    # def check_email(cls, value, db = Depends(get_db)):
    #     user = db.query(User).filter(
    #         User.email == value
    #     ).first()

    #     if user:
    #         raise ValueError("Email already exists")
    #     return value