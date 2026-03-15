from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models import User, Project
from schemas import ProjectCreate
from auth import logging

router = APIRouter(prefix="/project", tags=["Project"])

@router.post("/")
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):
    owner = db.query(User).filter(User.id == data.owner_id).first()
    if not owner:
        raise HTTPException(status_code=400, detail="Invalid owner_id")
    project = Project(
        name=data.name,
        description=data.description,
        owner_id=data.owner_id
    )
    try:
        db.add(project)
        db.commit()
        logging.info(f"Project created by user {data.owner_id}")
        return {"project_status": "Project created successfully"}
    except Exception as e:
        logging.error(f"Project creation failed for user {data.owner_id}")
        return {"error": str(e)}