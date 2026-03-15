from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserRegisterRequest(BaseModel):
    username: str = Field(..., max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=128)

class TokenRefreshRequest(BaseModel):
    refresh: str

class ProjectCreate(BaseModel):
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=500)
    owner_id: UUID

class TaskCreate(BaseModel):
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=500)
    project_id: UUID
    assigned_to: UUID

class CommentCreate(BaseModel):
    task_id: UUID
    comment_text: str = Field(..., max_length=1000)