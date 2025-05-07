from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    first_name: str
    last_name: str | None = None
    password: str


class UserLogin(UserBase):
    password: str


class UserDetail(UserBase):
    id: int
    first_name: str
    last_name: str | None = None
    is_active: bool
    is_admin: bool
    is_email_verified: bool

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access: str
    refresh: str
    type: str


class RefreshToken(BaseModel):
    refresh: str


class UserAuth(BaseModel):
    user: UserDetail
    token: Token
