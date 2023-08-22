from pydantic import BaseModel


class PermissionBaseSchema(BaseModel):
    title: str
    description: str | None = None


class PermissionCreateSchema(PermissionBaseSchema):
    pass

class PermissionSchema(PermissionBaseSchema):
    id: int

    class Config:
        orm_mode = True

