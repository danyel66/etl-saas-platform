from pydantic import BaseModel, EmailStr


# Shared base schema
class UserBase(BaseModel):
    email: EmailStr
    full_name: str


# Schema for user creation (extends UserBase)
class UserCreate(UserBase):
    password: str


# Schema for login (standalone)
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Schema for returning user data (extends UserBase)
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
