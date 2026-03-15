from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from db import get_db
from models import User, RefreshToken
from schemas import TokenRefreshRequest
from auth import HASHED_TOKEN, CREATE_ACCESS_TOKEN, CREATE_REFRESH_TOKEN

router = APIRouter(prefix="/refreshtoken", tags=["Auth"])

@router.post("/")
def refresh_token(data: TokenRefreshRequest, db: Session = Depends(get_db)):
    hashed = HASHED_TOKEN(data.refresh)
    stored = db.query(RefreshToken).filter(RefreshToken.token_hash == hashed).first()
    if not stored:
        raise HTTPException(status_code=400, detail="Invalid refresh token")
    if stored.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Refresh token expired")
    user = db.query(User).filter(User.id == stored.user_id).first()
    db.delete(stored)
    db.commit()
    return {
        "access_token": CREATE_ACCESS_TOKEN(user),
        "refresh_token": CREATE_REFRESH_TOKEN(user, db)
    }