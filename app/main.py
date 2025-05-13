# app/main.py

from fastapi import FastAPI, HTTPException, Depends
from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils import hash_password
from sqlalchemy.orm import Session


app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User signup route
@app.post("/signup/")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_password = hash_password(user.password)

    # Create new user in the database
    new_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "User created successfully", "user": {"email": new_user.email, "full_name": new_user.full_name}}
