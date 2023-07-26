import uuid
from unittest.mock import Mock, patch

import pytest
from fastapi.testclient import TestClient

from app.item.schema import ItemCreate
from main import app

client = TestClient(app)


@pytest.fixture
@patch("app.item.router.get_db")
def mock_get_db(db_mocker) -> Mock:
    return db_mocker


class TestItem:
    def test_post_item(self, mock_get_db) -> None:
        test_item = ItemCreate(title="Test Item", completed=False, deleted=False)

        mock_response_item = {
            "id": str(uuid.uuid4()),
            "title": "Test Item",
            "completed": False,
            "deleted": False,
        }

        with patch("app.item.router.create_item", return_value=mock_response_item):
            response = client.post("/items/", json=test_item.model_dump())

        assert response.status_code == 200
        assert response.json() == mock_response_item

    def test_get_single_item(self, mock_get_db) -> None:
        mock_response_item = {
            "id": str(uuid.uuid4()),
            "title": "Test Item",
            "completed": False,
            "deleted": False,
        }

        with patch("app.item.router.get_item", return_value=mock_response_item):
            response = client.get(f"/items/{mock_response_item['id']}")

        assert response.status_code == 200
        assert response.json() == mock_response_item

    def test_get_single_item_not_found(self, mock_get_db) -> None:
        mock_response_item = None

        with patch("app.item.router.get_item", return_value=mock_response_item):
            response = client.get(f"/items/{str(uuid.uuid4())}")

        assert response.status_code == 404
        assert response.json() == {"detail": "Item not found"}

    def test_get_all_items(self, mock_get_db) -> None:
        mock_response_items = [
            {
                "id": str(uuid.uuid4()),
                "title": "Test Item",
                "completed": False,
                "deleted": False,
            },
            {
                "id": str(uuid.uuid4()),
                "title": "Test Item",
                "completed": False,
                "deleted": False,
            },
        ]

        with patch("app.item.router.get_items", return_value=mock_response_items):
            response = client.get("/items/")

        assert response.status_code == 200
        assert response.json() == mock_response_items

    def test_get_all_items_with_completed(self, mock_get_db) -> None:
        mock_response_items = [
            {
                "id": str(uuid.uuid4()),
                "title": "Test Item",
                "completed": True,
                "deleted": False,
            },
            {
                "id": str(uuid.uuid4()),
                "title": "Test Item",
                "completed": True,
                "deleted": False,
            },
        ]

        with patch("app.item.router.get_items", return_value=mock_response_items):
            response = client.get("/items/?completed=true")

        assert response.status_code == 200
        assert response.json() == mock_response_items

    def test_get_all_items_with_deleted(self, mock_get_db) -> None:
        mock_response_items = [
            {
                "id": str(uuid.uuid4()),
                "title": "Test Item",
                "completed": False,
                "deleted": True,
            },
            {
                "id": str(uuid.uuid4()),
                "title": "Test Item",
                "completed": False,
                "deleted": True,
            },
        ]

        with patch("app.item.router.get_items", return_value=mock_response_items):
            response = client.get("/items/?deleted=true")

        assert response.status_code == 200
        assert response.json() == mock_response_items

    def test_update_item(self, mock_get_db) -> None:
        mock_response_item = {
            "id": str(uuid.uuid4()),
            "title": "Test Item",
            "completed": True,
            "deleted": False,
        }

        with patch("app.item.router.update_item", return_value=mock_response_item):
            response = client.put(
                f"/items/{mock_response_item['id']}",
                json=ItemCreate(
                    title="Test Item", completed=True, deleted=False
                ).model_dump(),
            )

        assert response.status_code == 200
        assert response.json() == mock_response_item

    def test_remove_item(self, mock_get_db) -> None:
        mock_response_item = {
            "id": str(uuid.uuid4()),
            "title": "Test Item",
            "completed": False,
            "deleted": False,
        }

        with patch("app.item.router.remove_item", return_value=mock_response_item):
            response = client.delete(f"/items/{mock_response_item['id']}")

        assert response.status_code == 200
        assert response.json() == mock_response_item
