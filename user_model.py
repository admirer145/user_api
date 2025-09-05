from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str
    age: int
    password: str = Field(..., min_length=6, max_length=12)



class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    