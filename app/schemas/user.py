from pydantic import BaseModel, EmailStr

# Pydantic model for user signup
class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str
class UserLogin(BaseModel):
    email: EmailStr
    password: str
