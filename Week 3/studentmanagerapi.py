from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict

app = FastAPI(title="Student Manager API")

students_db: Dict[int, dict] = {}

class Student(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., min_length=1, example="John Doe")
    age: int = Field(..., ge=3, le=120, example=20)
    major: str = Field(..., min_length=2, example="Computer Science")

@app.post("/students", response_model=Student, status_code=201)
def add_student(student: Student):
    if student.id in students_db:
        raise HTTPException(status_code=400, detail="Student with this ID already exists.")
    students_db[student.id] = student.dict()
    return student
@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Manager API. Visit /docs for Swagger UI."}

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    return student

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: Student):
    if student_id != updated_student.id:
        raise HTTPException(status_code=400, detail="ID in path and body must match.")
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found.")
    students_db[student_id] = updated_student.dict()
    return updated_student

@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found.")
    del students_db[student_id]
    return

@app.get("/students", response_model=dict)
def list_students():
    return students_db
