from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from infrastructure.database import Base

class ClientModel(Base):
    __tablename__ = "clients"

    client_id = Column(String, unique=True, index=True, primary_key=True)
    client_secret = Column(String)
    authorization_codes = relationship(
        "AuthorizationCodeModel",
        back_populates="client"
    )