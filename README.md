# Task Management System API (2026)

Backend REST API for managing projects, tasks, and team collaboration.

## Overview

Task Management System API is a backend service built for handling project workflows including user authentication, project management, task assignment, and comments. The system supports secure role-based access and structured relational data management.

## Features

* User Registration and Login
* JWT Authentication
* Role-Based Access Control
* Project Management
* Task Assignment and Tracking
* Comment System
* Ownership Validation
* Soft Delete for Data Safety
* Logging Support

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* JWT Authentication

## Database Design

Relational schema includes the following core tables:

* Users
* Roles
* Projects
* Tasks
* Comments

Relationships between entities are managed using SQLAlchemy ORM.

## API Capabilities

The system provides 20+ RESTful API endpoints including:

### Authentication

* Register User
* Login
* Refresh Token
* Verify User

### Project Management

* Create Project
* Update Project
* View Projects
* Delete Project

### Task Management

* Create Task
* Assign Task
* Update Task
* Delete Task
* View Tasks

### Comments

* Add Comment
* View Comments
* Delete Comment

## Security

* Password hashing
* JWT token authentication
* Role-based authorization
* Ownership validation for resource modification

## Project Structure

```
project/
│
├── routes/
│   ├── login.py
│   ├── reg.py
│   ├── refresh.py
│   ├── verify.py
│   ├── project.py
│   └── task.py
│
├── auth.py
├── db.py
├── models.py
├── schemas.py
├── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/Task_Management_System.git
cd Task_Management_System
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
uvicorn main:app --reload
```

API documentation will be available at:

```
http://127.0.0.1:8000/docs
```

## Deployment

The API can be deployed using cloud platforms with environment-based configuration. Example platforms include Render or other container-based hosting solutions.

## Author

Surya
Backend Developer | Python | FastAPI
