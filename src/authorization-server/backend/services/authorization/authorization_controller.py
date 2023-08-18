from services.user.user_service import verify_login
from schemas.authorization_code import AuthorizationCodeRequestBaseSchema
from fastapi import APIRouter, Depends, HTTPException

from infrastructure.database import SessionLocal, get_db
from ..client.client_service import *

authorization_router = APIRouter(
    tags=["auth"],
)

@authorization_router.post("/authorization-code")
def get_authorization_code(authorizationCodeRequest: AuthorizationCodeRequestBaseSchema, db: SessionLocal = Depends(get_db)):
    if (verify_login(db, authorizationCodeRequest.user.email, authorizationCodeRequest.user.password) is False):
        raise HTTPException(status_code=401,detail="invalid credentials, cannot generate authorization code")
    if (get_client(db, authorizationCodeRequest.client_id) is None):
        raise HTTPException(status_code=404,detail="client not found, cannot generate authorization code")
    return "token"