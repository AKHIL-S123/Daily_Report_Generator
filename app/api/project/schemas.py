from pydantic import BaseModel


"""schema for project model"""
class ProjectInfo(BaseModel):
    project_short_name:str
    project_name: str
    client_org :str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                
                    "project_short_name":"EF",
                    "project_name":"efficient",
                    "client_org":"unity org"
                }
            ]
        }
    }