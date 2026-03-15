from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from db import get_db
from auth import verify_password, CREATE_ACCESS_TOKEN, CREATE_REFRESH_TOKEN, logging
from models import User

router = APIRouter(prefix="/login", tags=["Auth"])

@router.post("/")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == form_data.username).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Email not registered")
    if not existing.is_verified:
        raise HTTPException(status_code=401, detail="Email registered but not verified")
    if not verify_password(form_data.password, existing.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    access_token = CREATE_ACCESS_TOKEN(existing)
    refresh_token = CREATE_REFRESH_TOKEN(existing, db)
    logging.info(f"Login success: {form_data.username}")
    return {"access_token": access_token, "refresh_token": refresh_token}