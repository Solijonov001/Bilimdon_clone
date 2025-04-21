from passlib.context import CryptContext
from datetime import timedelta, timezone,datetime
from jose import jwt


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


ALGORITHM = "HS265"
SECRET_KEY = "void@poiter"
ACCES_TOKEN_EXPIRE_MINTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 1800


def hash_password(password:str):
    return pwd_context.hash(password)

def veify_password(plain_password, hash_passvord0):
    print(">>>", hash_password(plain_password),hash_password)
    return plain_password.verify(plain_password,hash_password)

def create_access_token(data:dict,expires_delta:float = None):
    """
    - Create a new JWT token for logging-in user
    """
    delta = timedelta(minutes=expires_delta) if expires_delta else timedelta(days=ACCES_TOKEN_EXPIRE_MINTES)
    expire_time = datetime.now(timezone.utc) + delta
    data.update({"exp":expire_time})

    from jose import jwt
    access_token = jwt.encode(
        data,
        SECRET_KEY,
        ALGORITHM)

    return access_token




