from pydantic import BaseModel, EmailStr
from typing import Optional

# Shared base schema
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str]

# Schema for user creation (extends UserBase)
class UserCreate(UserBase):
    password: str
    role: Optional[str] = "user"

# Schema for login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema for returning user data (extends UserBase)
class UserOut(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True
