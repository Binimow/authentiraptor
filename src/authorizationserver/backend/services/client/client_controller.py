from schemas.client import ClientSchema
from fastapi import APIRouter, Depends, HTTPException

from schemas.user import UserCreateSchema, UserSchema

from .client_service import *
from infrastructure.database import SessionLocal, get_db
client_router = APIRouter(
    prefix="/client",
)

@client_router.get("/", response_model=ClientSchema)
def acquire_credential(db: SessionLocal = Depends(get_db)):
    db_client = create_client(db)
    return db_client