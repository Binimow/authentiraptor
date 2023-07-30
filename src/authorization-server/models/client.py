from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from infrastructure.database import Base

class ClientModel(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String, unique=True, index=True)
    client_secret = Column(String)