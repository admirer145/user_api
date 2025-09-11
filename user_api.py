from fastapi import APIRouter, Query, Path, HTTPException
from user_model import UserCreate, UserResponse, UserUpdate
from typing import List, Union, Dict

router = APIRouter()
id_counter = 1
global_user_dict = {}


@router.get("/")
async def get_all_user():
    return {"users": global_user_dict}


@router.get("/{id}", response_model=Union[UserResponse, Dict])
async def get_user_by_id(id: int = Path(..., gt=0)):
    if id not in global_user_dict:
        raise HTTPException(status_code=404, detail="Invalid id provided")
    user_resp = global_user_dict.get(id)
    return user_resp


@router.post("/", status_code=201, response_model=Dict[int, UserResponse])
async def create_user(user: UserCreate):
    global id_counter
    user_dict = user.model_dump()
    user_dict.update(id=id_counter)
    global_user_dict[id_counter] = user_dict
    id_counter += 1
    return global_user_dict


@router.put("/{id}")
async def update_user(id: int, user: UserUpdate):
    if id not in global_user_dict:
        raise HTTPException(status_code=404, detail=f"Invalid id provided: {id}")
    
    curr_user_dict = global_user_dict.get(id)
    curr_user_dict.update(user.model_dump())
    global_user_dict[id] = curr_user_dict
    return "Data updated successfully"


@router.delete("/{id}")
async def delete_user(id: int):
    if id not in global_user_dict:
        raise HTTPException(status_code=404, detail=f"Invalid id provided: {id}")
    
    del global_user_dict[id]

    return "Data deleted successfully"
