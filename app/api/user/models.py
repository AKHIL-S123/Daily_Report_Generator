from sqlalchemy import Column, Integer, String, Date,Interval, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from app.configuration.config import Base



class User(Base):
    ''' Get the user information from the database'''
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role =Column(String)
    refresh_token = Column(String)
    
    
    reports = relationship("UserReport", back_populates="user")
