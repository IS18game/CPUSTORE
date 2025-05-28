import pytest
from app import models

def test_search_products(client, db):
    # Создаём категорию и продукты
    category = models.Category(name="Test Category")
    db.add(category)
    db.commit()
    db.refresh(category)
    product1 = models.Product(name="Product 1", description="Desc 1", price=10.0, category_id=category.id)
    product2 = models.Product(name="Product 2", description="Desc 2", price=20.0, category_id=category.id)
    db.add_all([product1, product2])
    db.commit()

    # Тест поиска "Product 1"
    response = client.get("/products/search", params={"q": "Product 1"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Product 1"

    # Тест поиска "Desc 2"
    response = client.get("/products/search", params={"q": "Desc 2"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Product 2"

    # Тест поиска несуществующего термина
    response = client.get("/products/search", params={"q": "Non Existent"})
    assert response.status_code == 404