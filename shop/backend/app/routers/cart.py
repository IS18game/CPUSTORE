from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.cart import CartItem
from app.schemas.cart import CartItemCreate, CartItem as CartItemSchema

router = APIRouter(prefix="/cart", tags=["cart"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{user_id}", response_model=List[CartItemSchema])
def get_cart(user_id: int, db: Session = Depends(get_db)):
    cart_items = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    return cart_items


@router.post("/{user_id}/add", response_model=CartItemSchema, status_code=status.HTTP_201_CREATED)
def add_to_cart(user_id: int, cart_item: CartItemCreate, db: Session = Depends(get_db)):
    new_item = CartItem(user_id=user_id, product_id=cart_item.product_id, quantity=cart_item.quantity)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@router.put("/{user_id}/update/{item_id}", response_model=CartItemSchema)
def update_cart_item(user_id: int, item_id: int, cart_item: CartItemCreate, db: Session = Depends(get_db)):
    item = db.query(CartItem).filter(CartItem.id == item_id, CartItem.user_id == user_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Элемент корзины не найден.")
    item.product_id = cart_item.product_id
    item.quantity = cart_item.quantity
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{user_id}/delete/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cart_item(user_id: int, item_id: int, db: Session = Depends(get_db)):
    item = db.query(CartItem).filter(CartItem.id == item_id, CartItem.user_id == user_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Элемент корзины не найден.")
    db.delete(item)
    db.commit()
    return
