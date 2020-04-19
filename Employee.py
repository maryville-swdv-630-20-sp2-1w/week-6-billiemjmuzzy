from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Employee(Base):
    def __init__(self, role, first_name, last_name, hours):
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.hours = hours
        
    __tablename__ = 'employees'
    
    
    id = Column(Integer, primary_key=True)
    role = Column(String)
    first_name = Column(String)
    last_name= Column(String)
    hours = Column(Integer)
  
    
    
    def __repr__(self):
        return  f"Employee: role: {self.role}, first_name: {self.first_name}, last_name: {self.last_name}, hours: {self.hours}"
    
    
