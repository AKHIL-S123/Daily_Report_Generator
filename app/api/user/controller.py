from app.api.user.schemas import *
from app.api.user.service import *
from app.api.report.models import *
from app.utils.handler import *
from app.utils.bearer import *
from sqlalchemy.orm import Session
from fastapi import HTTPException


"""
@param - email - Email of the current logged user
@param - db -  Database Session object
@returns - User data object
"""


def user_exists(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


"""
@param - user_info - request body
@param - db -  database Session object
@returns - token and user data object
"""

def signup_controller(user_info:UserSchema, db: Session):
    db_user = user_exists(db, user_info.email)

    if db_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    else:
        signup_info=signup_service(db,user_info)
        return signup_info


"""
@param - user_info - request body
@param - db -  database Session object
@returns - token and user data object
"""

def login_controller(user_info:UserSchema, db: Session):
    db_user = user_exists(db, user_info.email) 

    if db_user:
        login_info=login_service(user_info,db,db_user)
        return login_info
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
        

"""
@param - refresh_token - Refresh token 
@param - db -  database session object
@returns - Refresh token 

"""

def refresh_token_controller(refresh_token: str, db: Session):
    decoded_token = decode_token(refresh_token)
    email = decoded_token.get("user_mail")
    role  = decoded_token.get("user_role")

    db_user = user_exists(db, email)
    if db_user:
        ref_token=refresh_token_service(refresh_token,db_user,email,role)
        return ref_token
    else:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    


