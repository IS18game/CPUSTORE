import pytest
from httpx import AsyncClient
from fastapi import status
from app.main import app
from app.database import SessionLocal, engine
from app.models import Base

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.mark.asyncio
async def test_register_and_login(test_client: AsyncClient = None):
    async with AsyncClient(app=app, base_url="http://test") as client:
        user_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "password": "testpassword"
        }
        response = await client.post("/auth/register", json=user_data)
        assert response.status_code == status.HTTP_201_CREATED
        user = response.json()
        assert user["username"] == user_data["username"]

        params = {"username": user_data["username"], "password": user_data["password"]}
        response = await client.post("/auth/login", params=params)
        assert response.status_code == status.HTTP_200_OK
        token_data = response.json()
        assert "access_token" in token_data
