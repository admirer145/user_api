from fastapi import APIRouter, Query, Path
from user_model import UserCreate, UserResponse
from typing import List

router = APIRouter()
id_counter = 3
user_list = [
    {
        "name": "Narendra",
        "age": 28,
        "id": 1,
        "password": "12892037hafdsjl"
    },
    {
        "name": "Govind",
        "age": 25,
        "id": 2,
        "password": "1213"
    }
]


@router.get("/")
def get_all_user():
    return {"users": user_list}


@router.get("/{id}")
def get_user_by_id(id: int = Path(..., gt=0), 
                   age: int = Query(..., ge=0, le=150)):
    for user in user_list:
        if user["id"] == id:
            return user
    return {}


@router.post("/", response_model=List[UserResponse])
def create_user(user: UserCreate):
    global id_counter
    user_dict = user.dict()
    user_dict.update(id=id_counter)
    id_counter += 1
    user_list.append(user_dict)

    return user_list
