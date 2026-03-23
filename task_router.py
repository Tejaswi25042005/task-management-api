from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.task import Task
from schemas.task_schema import TaskCreate, TaskUpdate
from database import engine
from models.task import Base

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        description=task.description
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"message": "Task not found"}

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}
@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):

    existing_task = db.query(Task).filter(Task.id == task_id).first()

    if not existing_task:
        return {"error": "Task not found"}

    existing_task.title = task.title
    existing_task.description = task.description

    db.commit()
    db.refresh(existing_task)

    return existing_task
@router.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    task.completed = True

    db.commit()
    db.refresh(task)

    return task