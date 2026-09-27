from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    name: str
    age: int

@app.get("/hello")
def hello():
    return {"message": "Hello, from FastAPI backend!"}

@app.post("/great_user")
def create_user(user_request: UserRequest):
    return {"message": f"User {user_request.name} of age {user_request.age} created successfully!"}    