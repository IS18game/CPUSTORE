from pydantic import BaseModel
from typing import Optional, List
from .review import Review  

class ProductBase(BaseModel):
    name: str
    category_id: int
    price: float
    description: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    rating: float
    reviews: List[Review] = []

    class Config:
        orm_mode = True
