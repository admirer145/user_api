from fastapi import APIRouter, Query, Path
from user_model import UserCreate, UserResponse
from typing import List, Union, Dict

router = APIRouter()
id_counter = 1
global_user_dict = {}


@router.get("/")
def get_all_user():
    return {"users": global_user_dict}


@router.get("/{id}", response_model=Union[UserResponse, Dict])
def get_user_by_id(id: int = Path(..., gt=0), 
                   age: int = Query(..., ge=0, le=150)):
    user_resp = global_user_dict.get(id)
    if user_resp is not None:
        return user_resp
    return {}


@router.post("/", response_model=Dict[int, UserResponse])
def create_user(user: UserCreate):
    global id_counter
    user_dict = user.dict()
    user_dict.update(id=id_counter)
    global_user_dict[id_counter] = user_dict
    id_counter += 1
    return global_user_dict
