from pydantic import BaseModel,Field,EmailStr
from enum import Enum
from typing import Optional
from datetime import date
from pydantic import validator
from fastapi import HTTPException



   
class InfoBase(BaseModel):
    ''' Request  data format '''
    date : date
    project: str
    task_id : str
    task :str
    status:str
    start_time:str
    end_time:str
    duration: Optional[float]
    description:str
    @validator('status')    
    def val_gen(cls,value):
        vaild=["Completed","RFD","InProgress"]
        if value not in vaild:
            raise HTTPException(status_code=400,detail="Status must be one of 'Completed','RFD','Inprogress")
        return value

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                
                    "date":"2023-09-01",
                    "project":"lotto",
                    "task_id":"123456789",
                    "task":"crud",
                    "status":"Completed",
                    "start_time":"10:00:00",
                    "end_time":"12:00:00",
                    "duration":2.0,
                    "description":"This is a description of the task.",
                }
            ]
        }
    }


