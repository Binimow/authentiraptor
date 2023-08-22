# def create_permission(db: Session, item: PermissionCreateSchema, user_id: int):
#     db_item = PermissionModel(**item.model_dump(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_itemdef create_permission(db:)

from authorizationserver.backend.models.permission import PermissionModel
from backend.schemas.permission import PermissionCreateSchema
from backend.infrastructure.database import SessionLocal


def create_permission(db: SessionLocal, permission: PermissionCreateSchema):
    db_permission = PermissionModel(**permission.model_dump())