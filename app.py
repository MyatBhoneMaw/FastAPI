from fastapi import FastAPI

# For Validation
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello Fast Api"}


@app.get("/users/{user_id}")
def detail(user_id: int):
    return {"hello", user_id}


class User(BaseModel):
    name: str
    age: int
    email: str


class UserResponse(BaseModel):
    name: str
    age: int


@app.post("/users", response_model=UserResponse)
def create_user(user: User):
    return user
