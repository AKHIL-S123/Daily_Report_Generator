from app.api.user.models import *
from app.api.user.schemas import *
from app.api.user.controller import *
from app.configuration.config import *
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from .response_definitions import *
user=APIRouter(tags=['User'])


@user.post('/signup',responses=signup)
async def signup_user(user_info:UserSchema, db: Session = Depends(get_db)):
    """To create a new user"""
    return signup_controller(user_info,db)

@user.post('/login',responses=login)
async def login(login_info:UserLoginSchema,db: Session = Depends(get_db)):
    """To sign-in """
    return login_controller(login_info,db)

@user.post("/user/refresh-token",responses=refresh__token)
async def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    """To get a new access token"""
    return refresh_token_controller(refresh_token, db)
