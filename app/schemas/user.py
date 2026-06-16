from pydantic import BaseModel, Field, EmailStr, field_validator
from fastapi import Depends
from app.dependencies import get_db
from app.models.user import User

class UserSchema(BaseModel):
    name:str = Field(min_length=3, max_length=50)
    email:EmailStr
    password: str = Field(min_length=8)

class LoginSchema(BaseModel):
    email:EmailStr
    password: str = Field(min_length=8)
   