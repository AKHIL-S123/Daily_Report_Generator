from app.api.user.schemas import *
from app.api.user.models import *
from app.api.user.controller import *
from app.utils.handler import *
from app.utils.bearer import *


"""
@param - user_info - request body
@param - db -  database Session object
@returns - token and user data object
"""

def signup_service(db,user_info):
    db_user = User(**user_info.__dict__)
    db.add(db_user)
    db.commit()

    access_token = sign_access_token(user_info.email,user_info.role)
    refresh_token = sign_refresh_token(user_info.email,user_info.role)
    db_user.refresh_token = refresh_token
    db.commit()
    

    access_token_expiration=calculate_utc_expiration(4*60*60)
    refresh_token_expiration=calculate_utc_expiration(24*60*60)
    user_info = {
        "user id" :db_user.id,
        "fullname": user_info.fullname,
        "email": user_info.email,
    }
    access_info = {
        "access_key":access_token,
        "expiry": access_token_expiration,
    }
    refresh_info={
        "refresh_key":refresh_token,
        "expiry": refresh_token_expiration,
    }

    return {"access_token":access_info,"refresh_token":refresh_info,"user_info":user_info}

"""
@param - user_info - request body
@param - db -  database Session object
@returns - token and user data object
"""

def login_service(user_info,db,db_user):
    access_token = sign_access_token(user_info.email,db_user.role)
    refresh_token = sign_refresh_token(user_info.email,db_user.role)
    db_user.refresh_token = refresh_token  
    db.commit()
    access_token_expiration=calculate_utc_expiration(4*60*60)
    refresh_token_expiration=calculate_utc_expiration(24*60*60)
    access_info = {
    "access_key":access_token,
    "expiry": access_token_expiration,
        }
    refresh_info={
    "refresh_key":refresh_token,
    "expiry": refresh_token_expiration,
    }
    user_info={
    "name":db_user.fullname,
    "email":db_user.email,
    "id":db_user.id,
    }
    return {"access_token": access_info, "refresh_token": refresh_info,"userdetail":user_info}

"""
@param - refresh_token - Refresh token 
@param - db -  database session object
@returns - Refresh token 

"""

def refresh_token_service(refresh_token,db_user,email,role):
    if db_user and db_user.refresh_token == refresh_token:
        access_token = sign_access_token(email,role)
        access_token_expiration=calculate_utc_expiration(4*60*60)
        access_info={
            "access_key":access_token,
            "expiry": access_token_expiration

        }

        return {"access_token": access_info}
    else:
        raise HTTPException(status_code=403, detail="Invalid token or expired token.")