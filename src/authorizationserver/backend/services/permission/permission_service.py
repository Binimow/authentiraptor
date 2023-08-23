# def create_permission(db: Session, item: PermissionCreateSchema, user_id: int):
#     db_item = PermissionModel(**item.model_dump(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_itemdef create_permission(db:)

from sqlalchemy import select
from models.permission import PermissionModel
from models.user import UserModel
from schemas.permission import PermissionCreateSchema
from sqlalchemy.orm import Session


def create_permission(db: Session, permission: PermissionCreateSchema):
    db_permission = PermissionModel(**permission.model_dump())
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission

def get_permission_by_title(db: Session, title: str):
    permission_by_name_db = select(PermissionModel).where(PermissionModel.title == title)
    return db.execute(permission_by_name_db).scalar()

def get_permission(db: Session, id: int):
    permission_db = select(PermissionModel).where(PermissionModel.id == id)
    return db.execute(permission_db).scalar()



def get_permissions(db: Session, skip: int = 0, limit: int = 100):
    permissions_stmt  = select(PermissionModel).offset(skip).limit(limit)
    return db.execute(permissions_stmt).scalars().all()