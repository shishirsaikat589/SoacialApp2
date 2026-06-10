from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    email: str
    username: str
    created_at: datetime

    class Config:
        from_attributes = True


class TokenOut(BaseModel):
    access_token: str
    token_type: str


class PostOut(BaseModel):
    id: int
    post_type: str
    content: Optional[str] = None
    file_path: Optional[str] = None
    caption: Optional[str] = None
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True
