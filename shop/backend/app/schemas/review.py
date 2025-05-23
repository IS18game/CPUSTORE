from pydantic import BaseModel


class ReviewBase(BaseModel):
    user_id: int
    product_id: int
    comment: str


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True
