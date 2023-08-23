from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.user import UserModel
from infrastructure.database import Base


class PermissionModel(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    users = relationship(
        "UserModel",
        secondary="user_permission"
    )
    # authorization_codes = relationship(
    #     "AuthorizationCodeModel",
    #     secondary="authorizationcode_permission"
    # )
