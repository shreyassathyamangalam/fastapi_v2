from pydantic import BaseModel, Field, StrictInt
from typing import Optional

# Define the Employee model
class Employee(BaseModel):
    id: int = Field(...,title="Employee ID", description="The unique identifier for the employee", gt=0)
    name: str = Field(...,title="Name of the Employee", description="The name of the employee", min_length=3, max_length=30)
    department: str = Field(...,title="Department of the Employee", description="The department of the employee", min_length=3, max_length=30)
    age: Optional[StrictInt] = Field(default=None, title="Employee Age", description="The age of the employee", ge=18, le=65)
    
