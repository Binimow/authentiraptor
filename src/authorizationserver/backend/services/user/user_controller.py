from fastapi import APIRouter, Depends, HTTPException
from services.permission.permission_service import get_permission

from schemas.user import UserCreateSchema, UserSchema, UserLoginSchema
from . import user_service

from infrastructure.database import SessionLocal, get_db

user_router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@user_router.get("/all/", response_model=list[UserSchema])
def get_users(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    return user_service.get_users(db=db, skip=skip, limit=limit)

@user_router.post("/login", response_model=UserSchema)
def login(user: UserLoginSchema, db: SessionLocal = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if not db_user:
        raise HTTPException(status_code=400, detail="Email not registered")
    if not user_service.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    return db_user

@user_router.put("/addpermission", response_model=UserSchema)
def add_user_permission(user_id: int, permission_id: int, db: SessionLocal = Depends(get_db)):
    db_user = user_service.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User id not registered")
    permission_db = get_permission(db=db, id=permission_id)
    if not permission_db:
        raise HTTPException(status_code=400, detail="Permission id not registered")
    user = user_service.assign_permission(db=db, user_id=user_id, permission_id=permission_id)
    return user

@user_router.post("/create/", response_model=UserSchema)
def create_user(user: UserCreateSchema, db: SessionLocal = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(db=db, user=user)