import datetime
from sqlalchemy import DateTime
from schemas.user import UserLoginSchema
from pydantic import BaseModel


class AuthorizationCodeRequestCreateSchema(BaseModel):
    user: UserLoginSchema
    client_id: str
    # redirect_uri: str
    # response_type: str
    scope: list[str]

class AuthorizationCodeRequestGetSchema(BaseModel):
    client_id: str
    code: str
    # redirect_uri: str
    # response_type: str
    expire_on: datetime.datetime
    scope: list[str]
