from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    first_name: str
    last_name: str
    password: str


class User(UserBase):
    id: int
    first_name: str
    last_name: str
    is_admin: int

    class Config:
        orm_mode = True
