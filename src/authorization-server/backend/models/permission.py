from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from infrastructure.database import Base


class PermissionModel(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    test = Column(String)

    owner = relationship("UserModel", back_populates="permissions")