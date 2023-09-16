from pydantic import BaseModel


"""Schema for user signup"""
class UserSchema(BaseModel):
    fullname: str
    email: str
    password: str 
    role: str

    model_config={
        "json_schema_extra" : {
            "example": 
    
                {
                "fullname": "John Smith",
                "email": "smith@gmail.com",
                "password": "weakpassword",
                "role":"user"
                }
            
        }}

"""Schema for user login"""
class UserLoginSchema(BaseModel):
    email: str
    password: str



    model_config = {
        "json_schema_extra": {
            "example": 
                {
                    "email": "a@gmail.com",
                    "password": "a"
                }
            
        }
    }
    