from fastapi import FastAPI

app = FastAPI()


@app.post("/users")
def user_create():
    pass


@app.get("/users")
def get_all_user():
    pass


@app.get("/users/{user_id}")
def get_user_detail():
    pass


@app.put("/users/update")
def update_user():
    pass


@app.delete("/users/{user_id}")
def delete_user():
    pass
