from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home_path():
    return {"bootcamp": "fastapi"}


@app.get("/user")
def user_data():
    user = {
        "Name": "Narendra",
        "Age": 28
    }
    return user


@app.get("/user/{id}")
def specific_user(id: int):
    user = {
        "Name": "Govind",
        "Age": 25,
        "id": id
    }
    return user

