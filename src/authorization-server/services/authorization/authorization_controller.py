from schemas.authorization_code import AuthorizationCodeRequestBaseSchema
from fastapi import APIRouter, Depends

from infrastructure.database import SessionLocal, get_db
from ..client.client_service import *

authorization_router = APIRouter(
    tags=["auth"],
)

@authorization_router.post("/pre_getauthorizationcode")
def get_authorization_code(authorizationCodeRequest: AuthorizationCodeRequestBaseSchema, db: SessionLocal = Depends(get_db)):
    if (get_client(db, authorizationCodeRequest.client_id) is None):
        return "client not found, cannot generate authorization code"
    return "token"