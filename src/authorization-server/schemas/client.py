from pydantic import BaseModel


class ClientSchema(BaseModel):
    client_id: str
    client_secret: str

