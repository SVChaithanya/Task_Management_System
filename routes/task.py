from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models import User, Project, Task
from schemas import TaskCreate
from auth import logging

router = APIRouter(prefix="/tasks", tags=["Task"])

@router.post("/")
def create_task(data: TaskCreate, db: Session = Depends(get_db)):
    assignee = db.query(User).filter(User.id == data.assigned_to).first()
    if not assignee:
        raise HTTPException(status_code=400, detail="Invalid assigned_to ID")
    project = db.query(Project).filter(Project.id == data.project_id).first()
    if not project:
        raise HTTPException(status_code=400, detail="Invalid project_id")
    task = Task(
        title=data.title,
        description=data.description,
        status=True,
        priority=True,
        project_id=data.project_id,
        assignee_id=data.assigned_to
    )
    try:
        db.add(task)
        db.commit()
        logging.info(f"Task assigned to {data.assigned_to}")
        return {"task_status": "Task created successfully"}
    except Exception as e:
        logging.error(f"Task creation failed for {data.assigned_to}")
        return {"error": str(e)}