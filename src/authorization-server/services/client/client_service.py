import secrets
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.client import ClientModel
from infrastructure.database import SessionLocal


def create_client(db: SessionLocal):
    client_id = secrets.token_hex(16)
    client_secret = secrets.token_hex(32)
    db_client = ClientModel(client_id=client_id, client_secret=client_secret)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: str):
    users_stmt  = select(ClientModel).where(ClientModel.client_id == client_id)
    return db.execute(users_stmt).scalars().first()