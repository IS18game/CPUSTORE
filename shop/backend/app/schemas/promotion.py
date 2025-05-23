from pydantic import BaseModel
from typing import Optional


class PromotionBase(BaseModel):
    title: str
    description: Optional[str] = None


class PromotionCreate(PromotionBase):
    pass


class Promotion(PromotionBase):
    id: int

    class Config:
        orm_mode = True
