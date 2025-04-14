from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Bank(Base):
    __tablename__ = "banks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(49), unique=True, index=True)
    
    # Relationship with branches
    branches = relationship("Branch", back_populates="bank")

class Branch(Base):
    __tablename__ = "branches"

    ifsc = Column(String(11), primary_key=True, index=True)
    bank_id = Column(Integer, ForeignKey("banks.id"))
    branch = Column(String(74))
    address = Column(String(195))
    city = Column(String(50))
    district = Column(String(50))
    state = Column(String(26))
    
    # Relationship with bank
    bank = relationship("Bank", back_populates="branches") 