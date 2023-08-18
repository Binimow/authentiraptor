from schemas.user import UserLoginSchema
from pydantic import BaseModel


class AuthorizationCodeRequestBaseSchema(BaseModel):
    user: UserLoginSchema
    client_id: str
    redirect_uri: str
    response_type: str
    scope: list[str]
