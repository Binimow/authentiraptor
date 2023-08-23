
from fastapi import APIRouter, Depends, HTTPException
from schemas.permission import PermissionCreateSchema, PermissionSchema

from . import permission_service
from infrastructure.database import SessionLocal, get_db

permission_router = APIRouter(
    prefix="/permission",
    tags=["permission"],
)

@permission_router.get("/all/", response_model=list[PermissionSchema])
def get_permissions(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    return permission_service.get_permissions(db=db, skip=skip, limit=limit)

@permission_router.post("/create/", response_model=PermissionSchema)
def create_permission(permission: PermissionCreateSchema, db: SessionLocal = Depends(get_db)):
    db_permission = permission_service.get_permission_by_title(db, title=permission.title)
    if db_permission:
        raise HTTPException(status_code=400, detail="Permission title already registered")
    return permission_service.create_permission(db=db, permission=permission)