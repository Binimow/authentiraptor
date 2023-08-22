from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from infrastructure.database import Base

class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    permissions = relationship("PermissionModel", secondary="user_permission")

class UserPermissionModel(Base):
    __tablename__ = "user_permission"
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        primary_key=True
    )
    permission_id = Column(
        Integer,
        ForeignKey("permissions.id"),
        primary_key=True
    )