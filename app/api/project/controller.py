from app.api.project.schemas import *
from app.api.project.service import *
from app.api.project.models import *
from app.api.report.models import *
from app.utils.handler import *
from app.utils.bearer import *
from fastapi import HTTPException
from sqlalchemy.orm import Session




"""
@param - data- Request body
@param - token - Verified token
@param - db -  Database Session object
@returns - Project Data object
"""

def create_project_controller(data:ProjectInfo,token,db):

    user = decode_token(token)
    if user["user_role"]=="admin":
        project=create_project_service(data,db)
        return project
    else:
        raise HTTPException(status_code=403, detail="User cannot create a project")

"""
@param - db -  Database Session object
@returns -Project data object
"""    
   
def get_project_controller(db):
    project_details=get_project_sevice(db)
    return project_details


"""
@param - project_id - Id of the project 
@param - data- Request body
@param - token - Verified token
@param - db -  database Session object
@returns - Updated project Data object
"""

def update_project_controller(project_id,data,token,db:Session):
    user = decode_token(token)
    if user["user_role"]=="admin":
        project=update_project_service(project_id,data,db)
        return project
    else:
        raise HTTPException(status_code=403,detail="Only admin can update projects details")

"""
@param - project_id - Id of the project 
@param - token - Verified token
@param - db -  Database Session object
@returns -  Project information successfully deleted
"""


def delete_project_controller(project_id,token,db:Session):
    user = decode_token(token)
    if user["user_role"]=="admin":
        project=delete_project_service(project_id,db)
        return project
    else:
        raise HTTPException(status_code=403,detail="Only admin can delete  projects details")




    
