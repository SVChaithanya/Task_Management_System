from fastapi import FastAPI
from routes import reg, login, verify, project, refresh, task

app = FastAPI(
    title="Multi-User Project Management API",
    description="Backend API for task and project management system with JWT authentication",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Task Management API is running"}

# Include routers
app.include_router(reg.router)
app.include_router(verify.router)
app.include_router(login.router)
app.include_router(refresh.router)
app.include_router(project.router)
app.include_router(task.router)
