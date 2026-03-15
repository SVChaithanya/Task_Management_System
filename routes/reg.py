from fastapi import APIRouter, Depends, HTTPException
from uuid import uuid4

from db import get_db,Session
from auth import hash_password, logging
from models import User
from schemas import UserRegisterRequest

router = APIRouter(prefix="/reg", tags=["Auth"])

@router.post("/")
def register(data: UserRegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Email already registered")
    verification_token = str(uuid4())
    new_user = User(
        username=data.username,
        email=data.email,
        password=hash_password(data.password),
        is_active=False,
        is_verified=False,
        verification_token=verification_token
    )
    try:
        db.add(new_user)
        db.commit()
        logging.info(f"user registered: {data.email}")
        return {"verification_token": verification_token, "status": f"{data.email} registered"}
    except Exception as e:
        logging.error(f"user registration failed: {data.email}")
        return {"error": str(e)}