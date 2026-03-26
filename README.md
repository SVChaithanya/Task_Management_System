# Task Management System API

Backend system design project — REST API with RBAC, cursor-based pagination, atomic transactions, and full CI.

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- JWT
- RBAC
- Alembic
- pytest
- GitHub Actions

---

## Overview

Fully featured task management backend across 4 domains: auth, projects, tasks, comments.
20+ REST endpoints. Built to demonstrate real backend system design — not just CRUD.

---

## System Design Highlights

### Schema Design
- 5-table normalised schema
- FK constraints and cascade deletes
- Soft delete via `deleted_at` column — data recovery without data loss
- Composite indexes on `(user_id, project_id)` and `(user_id, status)` — replaced full-table scans with index scans

---

### Pagination
- Cursor-based pagination — avoids loading full result sets into memory on large datasets

---

### Filtering
- Server-side filtering: status, priority, assigned_to, date range
- SQLAlchemy dynamic filter chaining — injection-safe, composable, no raw SQL

---

### Atomic Transactions
- Create task + write audit_log in a single transaction
- Audit failure rolls back task creation
- DB never left in a partial state

---

## Auth & Permissions

- JWT access + refresh tokens
- RBAC: admin bypasses ownership checks; regular users modify only their own tasks
- Alembic migrations for schema versioning

---

## Testing & CI

25 pytest tests covering:
- Registration and login
- JWT expiry
- Task CRUD
- Ownership boundary enforcement
- Admin bypass
- Soft delete and recovery
- Invalid payload handling

All tests run on every push via GitHub Actions (ubuntu-latest, Python 3.11)

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Register user |
| POST | /auth/login | Get JWT tokens |
| POST | /projects | Create project |
| GET | /projects/{id}/tasks | List tasks with filters + pagination |
| POST | /tasks | Create task |
| PATCH | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Soft delete task |
| POST | /tasks/{id}/comments | Add comment |

---

## Local Setup
```bash
git clone https://github.com/SVChaithanya/task-management-api
cd task-management-api
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload
```

Swagger UI: http://localhost:8000/docs

---

## Run Tests
```bash
pytest tests/ -v
```
