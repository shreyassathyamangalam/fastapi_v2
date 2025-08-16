from pydantic import BaseModel

# Define a Pydantic model for employee data
class Employee(BaseModel):
    id: int
    name: str
    department: str
    age: int

