from fastapi import FastAPI
from app.routers import product, auth, cart, promotion
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Интернет-магазин API", version="1.0")

app.include_router(product.router)
app.include_router(auth.router)
app.include_router(cart.router)
app.include_router(promotion.router)
