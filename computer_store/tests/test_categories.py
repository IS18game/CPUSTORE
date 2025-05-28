import pytest
from app import models

def test_create_category(client, db):
    response = client.post("/categories/", json={"name": "Test Category"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Category"

    category = db.query(models.Category).filter(models.Category.name == "Test Category").first()
    assert category is not None
    assert category.name == "Test Category"

def test_create_category_duplicate_name(client, db):
    response = client.post("/categories/", json={"name": "Test Category"})
    assert response.status_code == 200

    response = client.post("/categories/", json={"name": "Test Category"})
    assert response.status_code == 400

def test_get_categories(client, db):
    category1 = models.Category(name="Category 1")
    category2 = models.Category(name="Category 2")
    db.add_all([category1, category2])
    db.commit()

    response = client.get("/categories/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    names = [c["name"] for c in data]
    assert "Category 1" in names
    assert "Category 2" in names

def test_get_category(client, db):
    category = models.Category(name="Test Category")
    db.add(category)
    db.commit()
    db.refresh(category)

    response = client.get(f"/categories/{category.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Category"

    response = client.get("/categories/999")
    assert response.status_code == 404