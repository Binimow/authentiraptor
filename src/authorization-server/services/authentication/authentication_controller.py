from fastapi import APIRouter, Depends, HTTPException

from schemas.user import UserCreateSchema, UserSchema

from infrastructure.database import SessionLocal, get_db

authentication_router = APIRouter(
    tags=["auth"],
)

@authentication_router.get("/gettoken")
def get_token():
    return "token"