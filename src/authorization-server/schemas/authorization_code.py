from pydantic import BaseModel


class AuthorizationCodeRequestBaseSchema(BaseModel):
    client_id: str
    redirect_uri: str
    response_type: str
    scopes: list[str]
