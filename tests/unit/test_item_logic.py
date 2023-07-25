from unittest.mock import patch

import pytest

from app.item.logic import create_item
from app.item.schema import Item, ItemCreate


@pytest.fixture
@patch("app.item.logic.Session")
def mock_db_session(
    session,
):
    return session


class TestItemLogic:
    def test_create_item(self, mock_db_session) -> None:
        test_item = ItemCreate(title="Test Item", completed=False, deleted=False)

        mock_db_session.add.return_value = None
        mock_db_session.commit.return_value = None
        mock_db_session.refresh.return_value = None

        create_item(mock_db_session, test_item)

        mock_db_session.add.assert_called_once()
        mock_db_session.commit.assert_called_once()
        mock_db_session.refresh.assert_called_once()
