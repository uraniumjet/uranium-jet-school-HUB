from fastapi import FastAPI

app = FastAPI(
    title="Uranium SchoolHub API",
    description="School Management System for Northern Nigeria Schools",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Uranium SchoolHub"}