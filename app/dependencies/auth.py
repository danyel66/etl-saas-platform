from fastapi import Depends, HTTPException, status
from app.utils import verify_token
from app.models.user import User
from sqlalchemy.orm import Session
from app.database import get_db

def get_current_user(token: str = Depends(verify_token), db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.email == token["sub"]).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user

def require_role(required_role: str):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"User does not have the required '{required_role}' role"
            )
        return current_user
    return role_checker
