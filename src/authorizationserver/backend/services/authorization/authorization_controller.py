from schemas.authorization_code import AuthorizationCodeRequestCreateSchema
from services.authorization.authorization_service import create_authorizationcode
from services.user.user_service import get_user_by_email
from services.user.user_service import verify_login
from schemas.authorization_code import AuthorizationCodeRequestGetSchema
from fastapi import APIRouter, Depends, HTTPException

from infrastructure.database import SessionLocal, get_db
from ..client.client_service import *

authorization_router = APIRouter(
    tags=["auth"],
)

@authorization_router.post("/authorization-code", response_model=AuthorizationCodeRequestGetSchema)
def get_authorization_code(authorization_code_request: AuthorizationCodeRequestCreateSchema, db: SessionLocal = Depends(get_db)):
    print('here')
    if (verify_login(db, authorization_code_request.user.email, authorization_code_request.user.password) is False):
        raise HTTPException(status_code=401,detail="invalid credentials, cannot generate authorization code")
    if (get_client(db, authorization_code_request.client_id) is None):
        raise HTTPException(status_code=404,detail="client not found, cannot generate authorization code")
    user = get_user_by_email(db, authorization_code_request.user.email)
    print(user)
    if (user == None):
        raise HTTPException(status_code=404, detail="user not found")
    if(not all(scope in [permission.title for permission in user.permissions] for scope in authorization_code_request.scope)):
        raise HTTPException(status_code=401, detail="Specified user doesn't have the required permissions for the provided scope")
    authorizationcode_db = create_authorizationcode(db, authorization_code_request.scope, authorization_code_request.client_id)
    authorizationcode_dto = AuthorizationCodeRequestGetSchema(
        client_id=authorizationcode_db.client_id,
        expire_on=authorizationcode_db.expire_on,
        scope=[permission.title for permission in authorizationcode_db.scope]
    )
    print(f"{authorizationcode_dto.__dict__}")
    return authorizationcode_dto