from fastapi import APIRouter, Depends, HTTPException

from schemas.user import UserCreateSchema, UserSchema
from . import user_service

from infrastructure.database import SessionLocal, get_db

user_router = APIRouter(
    tags=["user"],
)

@user_router.get("/users/", response_model=list[UserSchema])
def get_users(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    return user_service.get_users(db=db, skip=skip, limit=limit)

@user_router.post("/user/", response_model=UserSchema)
def create_user(user: UserCreateSchema, db: SessionLocal = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(db=db, user=user)