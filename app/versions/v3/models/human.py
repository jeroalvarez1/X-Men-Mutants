from sqlalchemy import Column, Integer, Boolean, ARRAY, String
from app.database import Base

class Human(Base):
    __tablename__ = 'human'
    id = Column(Integer, primary_key=True)
    dna = Column(ARRAY(String))
    is_mutant = Column(Boolean)