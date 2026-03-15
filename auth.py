import os, uuid, hashlib, logging
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from sqlalchemy.orm import Session
from models import User, RefreshToken
from db import get_db

# JWT settings
security = os.getenv("SECURITY_KEY")
if not security:
    raise RuntimeError("SECURITY_KEY not found")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_MIN = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
REFRESH_TOKEN_DAY = 7

# Logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/test.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str):
    return pwd_context.hash(password)
def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)

# JWT tokens
def CREATE_ACCESS_TOKEN(user: User):
    jti = str(uuid.uuid4())
    payload = {
        "sub": user.email,
        "user_id": str(user.id),
        "jti": jti,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_MIN)
    }
    return jwt.encode(payload, security, algorithm=ALGORITHM)

def HASHED_TOKEN(token: str):
    return hashlib.sha256(token.encode()).hexdigest()

def CREATE_REFRESH_TOKEN(user: User, db: Session):
    raw_token = str(uuid.uuid4())
    hashed_token = HASHED_TOKEN(raw_token)
    refresh = RefreshToken(
        user_id=user.id,
        token_hash=hashed_token,
        expires_at=datetime.utcnow() + timedelta(days=REFRESH_TOKEN_DAY)
    )
    db.add(refresh)
    db.commit()
    db.refresh(refresh)
    return raw_token
