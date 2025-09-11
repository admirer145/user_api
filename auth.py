from fastapi import APIRouter, Header
import jwt
import os
router = APIRouter()

user_to_token_dict = {}

SECRET_KEY = os.getenv("SECRET_KEY")


@router.get("/generate_token/{user_id}")
def generate_token(user_id: str):

    if user_id in user_to_token_dict:
        return user_to_token_dict[user_id]

    jwt_token = jwt.encode(payload={"user_id": user_id}, key=SECRET_KEY, algorithm="HS256")

    user_to_token_dict[user_id] = jwt_token

    return {"token": jwt_token}


@router.get("/validate")
def validate(token: str = Header(...)):
    print(token)
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms="HS256")
    except Exception:
        return "Invalid token provided"

    return payload
