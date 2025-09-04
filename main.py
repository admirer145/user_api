from fastapi import FastAPI

from typing import Optional, Union, Annotated

app = FastAPI()

@app.get("/")
def home_path():
    return {"bootcamp": "fastapi"}


user_list = [
    {
        "Name": "Narendra",
        "Age": 28,
        "id": 1
    },
    {
        "Name": "Govind",
        "Age": 25,
        "id": 2
    }
]

@app.get("/user")
def get_all_user(age: int, name: Union[str, int] = None):
    user_list_filter = []
    for user in user_list:
        if user["Age"] > age:
            user_list_filter.append(user)
    return {"users": user_list_filter}


@app.get("/user/{id}")
def get_user_by_id(id: int):
    for user in user_list:
        if user["id"] == id:
            return user
    return {}
