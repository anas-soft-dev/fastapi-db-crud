
import jwt
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

SECRET_KEY = "DATABASE123@HS256"
ALGORITHM = "HS256"
EXPIRE_TIME = 30

session = HTTPBearer()


def create_access_token(data:dict):
    payload = data.copy()

    expiry_time = datetime.now(timezone.utc) + timedelta(
        minutes=EXPIRE_TIME
    )

    payload["exp"]=expiry_time

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def check_access_token(credentials: HTTPAuthorizationCredentials = Depends(session)):

    try:
        token = credentials.credentials
        data = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=ALGORITHM
        )

        return data
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token Expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )


