from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/products",
    tags=["products"],
)

@router.get("/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@router.get("/search", response_model=list[schemas.Product])
def search_products_route(q: str = "", db: Session = Depends(get_db)):
    if not q.strip():
        return []
    products = crud.search_products(db, q.strip())
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/category/{category_id}", response_model=list[schemas.Product])
def get_products_by_category_route(category_id: int, db: Session = Depends(get_db)):
    products = crud.get_products_by_category(db, category_id)
    if not products:
        raise HTTPException(status_code=404, detail="No products found in this category")
    return products