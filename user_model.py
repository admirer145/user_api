from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime
import pytz


class Address(BaseModel):
    city: str
    state: str
    pincode: str

    @field_validator("pincode")
    def pincode_validate(cls, v):
        if (len(v) != 6 ) or (not v.isdigit()):
            raise ValueError("pincode must be six letter")
        return v
    
    @model_validator(mode="before")
    def multi_validate(cls, d):
        states = d.get("state")
        state_list = ["mp", "up", "string"]
        if states not in state_list:
            raise ValueError("Invalid state provided")
        return d


class UserBase(BaseModel):
    name: str
    age: int
    address: Address



class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=12)
   


def calculate_time():
    time_now = datetime.now()
    time_now.astimezone(tz=pytz.timezone("Asia/Kolkata"))
    return time_now


class UserResponse(UserBase):
    id: int
    date_created: datetime = Field(default_factory=calculate_time)
