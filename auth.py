from fastapi import APIRouter, Header
import jwt

router = APIRouter()


SECRET_KEY = '63b642155d5d19da1171e1d5e72b32458d2d1c1247fa154a183e3a0fb0c1c7b2'

user_to_token_dict = {}


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
