from sqlalchemy import Column, Integer, String, DateTime
from app.configuration.config import Base
from datetime import datetime
import pytz  
ist = pytz.timezone('Asia/Kolkata')


class ProjectTable(Base):
    """ Store and get the project information from the database """
    __tablename__="projects_info"
    id = Column(Integer,primary_key=True,index=True)
    project_short_name= Column(String)
    project_name= Column(String)
    client_org =Column(String)
    created_date = Column(DateTime, default=datetime.now(ist))
    updated_At = Column(DateTime, default=lambda: datetime.now(ist), onupdate=lambda: datetime.now(ist))