from pydantic import BaseModel, Field, EmailStr, field_validator
from fastapi import Depends
from app.dependencies import get_db

class PostSchema(BaseModel):
    title:str = Field(min_length=3, max_length=50)
    description:str
    category_id:int
    user_id:int