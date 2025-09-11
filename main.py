from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from user_api import router as user_router
from github_api import router as github_router
from auth import router as auth_router

app = FastAPI()

@app.get("/")
async def home_path():
    return {"bootcamp": "fastapi"}


# handler, custom raise 

@app.exception_handler(HTTPException)
async def custom_error_handler(req, exc: HTTPException):

    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail, "additonal": "some value"})



app.include_router(user_router, prefix="/users", tags=["Users"])

app.include_router(github_router, tags=["Github"])

app.include_router(auth_router, tags=["Auth"])
