from app.api.project.schemas import *
from app.api.project.models import *
from app.api.project.controller import *
from app.utils.handler import *
from app.utils.bearer import *
from datetime import  datetime
from fastapi import HTTPException


"""
@param - data- Request body
@param - token - Verified token
@param - db -  Database Session object
@returns - Project Data object
"""
def create_project_service(data,db):
    db_info = ProjectTable(
            
            project_short_name=data.project_short_name,
            project_name=data.project_name,
            client_org =data.client_org,
            created_date=datetime.now(ist),
        )
    db.add(db_info)
    db.commit()
    db.refresh(db_info)
    return db_info

"""
@param - db -  Database Session object
@returns -Project data object
"""   
def get_project_sevice(db):
    project_info=db.query(ProjectTable).all()
    return project_info

"""
@param - project_id - Id of the project 
@param - data- Request body
@param - token - Verified token
@param - db -  database Session object
@returns - Updated project Data object
"""
def update_project_service(project_id,data,db):
    project_info=db.query(ProjectTable).filter(ProjectTable.id==project_id).first()
    if project_info:
        project_info.project_short_name=data.project_short_name
        project_info.project_name = data.project_name
        project_info.client_org = data.client_org
        db.commit()
        db.refresh(project_info)
        return project_info
    raise HTTPException(status_code=404, detail="Project not found")
"""
@param - project_id - Id of the project 
@param - token - Verified token
@param - db -  Database Session object
@returns -  Project information successfully deleted
"""

def delete_project_service(project_id,db):
    project_info=db.query(ProjectTable).filter(ProjectTable.id==project_id).first()
    if project_info:
        db.delete(project_info)
        db.commit()
        return {"message":" Project information successfully deleted"}
    raise HTTPException(status_code=404, detail="Project not found")



