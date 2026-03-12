#!/usr/bin/env python3
"""Task Management API with FastAPI"""
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from datetime import datetime

# Database setup
engine = create_engine("sqlite:///tasks.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Models
class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500))
    status = Column(String(20), default="todo")
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# Schemas
class TaskCreate(BaseModel):
    title: str
    description: str = None
    status: str = "todo"

class TaskResponse(TaskCreate):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

# FastAPI app
app = FastAPI(title="Task Management API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks/", response_model=TaskResponse)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = TaskDB(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/", response_model=list[TaskResponse])
async def get_tasks(db: Session = Depends(get_db)):
    return db.query(TaskDB).all()

@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"status": "deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
