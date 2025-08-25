from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models, schemas, crud
from typing import List

# Define engine and bind metadata
Base.metadata.create_all(bind=engine)

# Define the FastAPI app
app = FastAPI()

# Create dependency with the DB for CRUD operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create API endpoints
# 1. Create an Employee Endpoint
@app.post('/employees', response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session=Depends(get_db)):
    return crud.create_employee(db, employee)

# 2. Get all Employees
@app.get('/employees', response_model=List[schemas.EmployeeOut])
def get_employees(db: Session=Depends(get_db)):
    return crud.get_employees(db)

# 3. Get a specific Employee
@app.get('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session=Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return employee

# 4. Update an Employee
@app.put('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session=Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return db_employee

# 5. Delete an Employee
@app.delete('/employees/{emp_id}', response_model=dict)
def delete_employee(emp_id: int, db: Session=Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    return {'detail': 'Employee Deleted'}

