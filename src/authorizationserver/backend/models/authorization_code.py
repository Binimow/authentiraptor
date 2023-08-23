from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from infrastructure.database import Base


class AuthorizationCodeModel(Base):
    __tablename__ = "authorizationcodes"

    id = Column(Integer, primary_key=True, index=True)
    scope = relationship(
        "PermissionModel",
        secondary="authorizationcode_permission"
    )
    expire_on = Column(DateTime)
    client = relationship(
        "ClientModel"
    )
    client_id = Column(String, ForeignKey("clients.client_id"))

class AuthorizationCodePermissionModel(Base):
    __tablename__ = "authorizationcode_permission"
    authorization_code_id = Column(
        Integer,
        ForeignKey("authorizationcodes.id"),
        primary_key=True
    )
    permission_id = Column(
        Integer,
        ForeignKey("permissions.id"),
        primary_key=True
    )