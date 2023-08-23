import secrets
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.permission import PermissionModel
from models.authorization_code import AuthorizationCodeModel
from datetime import datetime, timedelta

from infrastructure.database import SessionLocal
from ..client.client_service import get_client

def create_authorizationcode(db: Session, scopes: list[str], client_id: str):
    permissions_stmt = select(PermissionModel).where(PermissionModel.title in scopes)
    permissions_db  = db.execute(permissions_stmt).scalars().all()
    code = secrets.token_hex(16)
    authorizationcode_db = AuthorizationCodeModel(scope=permissions_db, 
                                                  expire_on=datetime.now() + timedelta(minutes = 10),
                                                  client_id=client_id,
                                                  code=code)
    db.add(authorizationcode_db)
    db.commit()
    db.refresh(authorizationcode_db)
    return authorizationcode_db