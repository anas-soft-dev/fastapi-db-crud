from pydantic import BaseModel, Field, EmailStr, field_validator
from fastapi import Depends
from app.dependencies import get_db
from app.models.user import User

class CategorySchema(BaseModel):
    title:str = Field(min_length=3, max_length=50)
    order:int = Field(gt=-1,ls=11)