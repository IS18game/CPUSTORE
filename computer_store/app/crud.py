from sqlalchemy.orm import Session
from sqlalchemy import or_
from . import models, schemas

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    category = db.query(models.Category).filter(models.Category.id == product.category_id).first()
    if not category:
        raise ValueError("Category does not exist")
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def search_products(db: Session, query: str):
    if not query:
        return []
    return db.query(models.Product).filter(
        or_(
            models.Product.name.ilike(f"%{query}%"),
            models.Product.description.ilike(f"%{query}%")
        )
    ).all()

def get_products_by_category(db: Session, category_id: int):
    return db.query(models.Product).filter(models.Product.category_id == category_id).all()