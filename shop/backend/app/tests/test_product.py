import pytest
from httpx import AsyncClient
from fastapi import status
from app.main import app
from app.database import SessionLocal, engine
from app.models import Base
from app.models.category import Category

@pytest.fixture(scope="module")
def test_client():
    # Используем AsyncClient для тестирования асинхронных эндпоинтов
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    category = Category(name="Test Category")
    db.add(category)
    db.commit()
    db.refresh(category)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.mark.asyncio
async def test_create_and_get_product(test_client):
    product_data = {
        "name": "Test Product",
        "category_id": 1,
        "price": 9.99,
        "description": "This is a test product."
    }
    response = await test_client.post("/products/", json=product_data)
    assert response.status_code == status.HTTP_201_CREATED
    product = response.json()
    assert product["name"] == product_data["name"]

    response = await test_client.get("/products/")
    assert response.status_code == status.HTTP_200_OK
    products = response.json()
    assert any(p["name"] == product_data["name"] for p in products)
