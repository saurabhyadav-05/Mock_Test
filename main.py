from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@app.post("/students", response_model=schemas.StudentResponse)
def create(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

# READ ALL + FILTER
@app.get("/students")
def get_all(course: str = None, db: Session = Depends(get_db)):
    return crud.get_students(db, course)

# READ ONE
@app.get("/students/{id}")
def get_one(id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, id)
    if not student:
        raise HTTPException(status_code=404, detail="Not found")
    return student

# UPDATE
@app.put("/students/{id}")
def update(id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.update_student(db, id, student)

# DELETE
@app.delete("/students/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db, id)