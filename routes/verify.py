from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models import User

router = APIRouter(prefix="/verify", tags=["Auth"])

@router.post("/")
def verify_user(token: str, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.verification_token == token).first()
    if existing:
        existing.is_active = True
        existing.is_verified = True
        db.commit()
        return {"verification_status": "User verified successfully"}
    raise HTTPException(status_code=404, detail="Invalid token")