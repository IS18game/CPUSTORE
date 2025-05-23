from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.models import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    price = Column(Float, nullable=False)
    rating = Column(Float, default=0.0)
    description = Column(Text)

    category = relationship("Category", backref="products")
    reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")
