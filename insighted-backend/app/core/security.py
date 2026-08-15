from datetime import datetime, timedelta

from jose import jwt

from app.database.config import SECRET_KEY
from jose import jwt, JWTError

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60
def create_access_token(data: dict):
    print("CREATE_ACCESS_TOKEN CALLED")

    to_encode = data.copy()

    expire = (
        datetime.utcnow()
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )
    print("EXP:", expire)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    print("TOKEN EXPIRES IN:", ACCESS_TOKEN_EXPIRE_MINUTES)

    return encoded_jwt
def verify_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        return None