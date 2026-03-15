from fastapi import FastAPI
from routes import reg, login, verify, project, refresh, task

app = FastAPI(title="Multi-User Project Management API")

# Include routers
app.include_router(reg.router)
app.include_router(verify.router)
app.include_router(login.router)
app.include_router(refresh.router)
app.include_router(project.router)
app.include_router(task.router)