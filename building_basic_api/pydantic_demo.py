from fastapi import FastAPI
from pydantic import BaseModel

# Define a Pydantic model
class User(BaseModel):
    id: int
    name: str

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route that uses the Pydantic model
@app.get("/user", response_model=User)
def get_user():
    return User(id=1, name="John Doe")

