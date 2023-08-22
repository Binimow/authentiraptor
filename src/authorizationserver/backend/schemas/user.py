from pydantic import BaseModel

from schemas.permission import PermissionSchema

class UserBaseSchema(BaseModel):
    email: str

class UserCreateSchema(UserBaseSchema):
    password: str

class UserLoginSchema(UserBaseSchema):
    password: str

class UserSchema(UserBaseSchema):
    id: int
    permissions: list[PermissionSchema] = []

    class Config:
        orm_mode = True