from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from app.api.project.models import *
from app.api.project.schemas import *
from app.api.project.controller import *
from app.configuration.config import *
from app.utils.bearer import JWTBearer
from .response_definition import *


project=APIRouter(tags=["Project"])


@project.post('/projects-info',responses=create_project_response) 
def create_project(data:ProjectInfo,token:str=Depends(JWTBearer()),db:Session=Depends(get_db)):
    """to create a new project"""
    return create_project_controller(data,token,db,)

@project.get('/projects-info',responses=get_project_response)
def get_project(token:str=Depends(JWTBearer()),db:Session=Depends(get_db)):
    """to get a project from the db"""
    return get_project_controller(db)  

@project.put('/projects-info/{project_id}',responses=update_project_response)
def update_project(project_id:int,data:ProjectInfo,token:str=Depends(JWTBearer()),db:Session=Depends(get_db)):
    """to update a project"""
    return update_project_controller(project_id,data,token,db)

@project.delete('/projects-info/{project_id}',responses=delete_project_respose)
def delete_project(project_id:int,token:str=Depends(JWTBearer()),db:Session=Depends(get_db)):
    """to delete project"""
    return delete_project_controller(project_id,token,db)