from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from user_api import router as user_router

app = FastAPI()

@app.get("/")
def home_path():
    return {"bootcamp": "fastapi"}


# handler, custom raise 

@app.exception_handler(HTTPException)
def custom_error_handler(req, exc: HTTPException):

    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail, "additonal": "some value"})



app.include_router(user_router, prefix="/users", tags=["Users"])
