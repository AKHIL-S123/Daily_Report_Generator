from fastapi import HTTPException
from datetime import datetime,timedelta
from decouple import config
import time
import jwt
import pytz

UTC=pytz.utc

def calculate_utc_expiration(expires_in:int):
    return datetime.now()+timedelta(seconds=expires_in)


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")



REFRESH_TOKEN_EXPIRATION = 24 * 60 * 60 *60
ACCESS_TOKEN_EXPIRATION = 4 * 60 * 60 *60



def sign_access_token(mail: str,role:str):  # 4 hours 
    payload = {
        "user_mail": mail,
        "user_role":role,
        "exp": time.time() + ACCESS_TOKEN_EXPIRATION
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def sign_refresh_token(mail: str,role:str):
    payload = {
        "user_mail": mail,
        "user_role":role,
        "exp": time.time() + REFRESH_TOKEN_EXPIRATION,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token 
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Token is invalid")
    


