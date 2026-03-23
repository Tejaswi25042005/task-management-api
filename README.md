# Task Management API

A backend REST API built using FastAPI to manage tasks with CRUD operations and task completion functionality.

## Features
- Create tasks
- Get all tasks
- Update tasks
- Delete tasks
- Mark tasks as completed

## Technologies Used
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Project Structure
task-management-backend/
│
├── models/
├── routers/
├── schemas/
├── database.py
├── main.py
├── requirements.txt
└── tasks.db

## Installation

Clone the repository:
git clone https://github.com/your-username/task-management-api.git

Navigate to project folder:
cd task-management-api

Install dependencies:
pip install -r requirements.txt

Run the server:
uvicorn main:app --reload

## API Documentation

Open in browser:
http://127.0.0.1:8000/docs

FastAPI Swagger UI will appear to test APIs.

## Author
Tejaswi Yadlapalli
