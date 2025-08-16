from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a simple route
@app.get("/")
def home():
    return {"message": "Hello, World!"}

