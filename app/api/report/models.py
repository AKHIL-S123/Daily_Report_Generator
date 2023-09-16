from sqlalchemy import Column, Integer, String, Date,Interval, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from app.configuration.config import Base
from datetime import datetime
import pytz  
ist = pytz.timezone('Asia/Kolkata')




class UserReport(Base):
    ''' Get the user report information from the database'''
    __tablename__ = "user_report"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    date = Column(Date)
    project = Column(String)
    task_id = Column(String)
    task = Column(String)
    status = Column(String)
    start_time = Column(String, nullable=False)
    end_time = Column(String)
    duration = Column(Interval)
    description = Column(String)
    created_date = Column(DateTime, default=datetime.now(ist))
    updated_At = Column(DateTime, default=lambda: datetime.now(ist), onupdate=lambda: datetime.now(ist))

  
    user = relationship("User", back_populates="reports")
