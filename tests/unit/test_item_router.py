import uuid
from unittest.mock import patch, Mock

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
    def test_post_item(self, mock_get_db):
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
