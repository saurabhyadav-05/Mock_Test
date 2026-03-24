from sqlalchemy.orm import Session
import models

# 🔹 GET ALL STUDENTS (with optional course filter)
def get_students(db: Session, course: str = None):
    query = db.query(models.Student)
    
    if course:
        query = query.filter(models.Student.course == course)
    
    return query.all()


# 🔹 GET SINGLE STUDENT
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


# 🔹 CREATE STUDENT
def create_student(db: Session, student):
    db_student = models.Student(**student.dict())
    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    
    return db_student


# 🔹 UPDATE STUDENT (supports partial update)
def update_student(db: Session, student_id: int, data):
    student = get_student(db, student_id)
    
    if not student:
        return None

    # Update only provided fields
    if hasattr(data, "name") and data.name is not None:
        student.name = data.name
    if hasattr(data, "age") and data.age is not None:
        student.age = data.age
    if hasattr(data, "course") and data.course is not None:
        student.course = data.course

    db.commit()
    db.refresh(student)

    return student


# 🔹 DELETE STUDENT
def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)
    
    if not student:
        return None

    db.delete(student)
    db.commit()

    return student


# 🔹 SEARCH STUDENTS BY NAME (BONUS)
def search_students(db: Session, keyword: str):
    return db.query(models.Student).filter(
        models.Student.name.ilike(f"%{keyword}%")
    ).all()