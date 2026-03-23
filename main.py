from fastapi import FastAPI
from database import engine, Base
from routers.task_router import router as task_router

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(task_router)