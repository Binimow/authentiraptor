from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from models.user import UserModel
from models.permission import PermissionModel
from schemas.user import UserCreateSchema
from schemas.permission import PermissionCreateSchema
import hashlib

# stmt stands for statement

def get_user(db: Session, user_id: int):
    return db.execute(
        select(UserModel).where(UserModel.id == user_id)
    ).scalars().all()

def get_user_by_email(db: Session, email: str):
    user_by_email_stmt = select(UserModel).where(UserModel.email == email)
    return db.execute(user_by_email_stmt).scalars().first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    users_stmt  = select(UserModel).offset(skip).limit(limit)
    return db.execute(users_stmt).scalars().all()


def create_user(db: Session, user: UserCreateSchema):
    hashed_password = hash_password(user.password)
    db_user = UserModel(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PermissionModel).offset(skip).limit(limit).all()


# def create_permission(db: Session, item: PermissionCreateSchema, user_id: int):
#     db_item = PermissionModel(**item.model_dump(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


def hash_password(password: str):
    return hashlib.sha3_256(password.encode('utf-8')).hexdigest()

def verify_password(password: str, hashed_password: str):
    return hash_password(password) == hashed_password

def verify_login(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user is None:
        return False
    return verify_password(password, user.hashed_password)
