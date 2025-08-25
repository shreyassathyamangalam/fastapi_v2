from pydantic import BaseModel, EmailStr

# Define Employee class
class EmployeeBase(BaseModel):
    name: str
    email: EmailStr

# Define class to create an Employee record
class EmployeeCreate(EmployeeBase):
    pass 

# Define a class to update an Employee record
class EmployeeUpdate(EmployeeBase):
    pass

# Define a class to retreive an Employee record
class EmployeeOut(EmployeeBase):
    id: int
    
    class Config():
        orm_mode = True
