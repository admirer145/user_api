from fastapi import FastAPI
from user_api import router as user_router

app = FastAPI()

@app.get("/")
def home_path():
    return {"bootcamp": "fastapi"}


app.include_router(user_router, prefix="/users", tags=["Users"])
