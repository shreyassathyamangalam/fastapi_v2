from fastapi import FastAPI

# Create the FastAPI app instance
app = FastAPI()

# Define a simple route
@app.get("/")
def index():
    return {"message": "Hello, World!"}
