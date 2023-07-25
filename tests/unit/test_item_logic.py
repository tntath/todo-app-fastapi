import uuid
from unittest.mock import patch, Mock

import pytest

from app.item.logic import create_item, get_item, get_items
from app.item.schema import Item, ItemCreate

TEST_ITEM_ID = uuid.uuid4()
TEST_ITEM = Item(id=TEST_ITEM_ID, title="Test Item", completed=False, deleted=False)


@pytest.fixture
@patch("app.item.logic.Session")
def mock_db_session(session) -> Mock:
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

    def test_get_item(self, mock_db_session) -> None:
        mock_db_session.query.return_value.filter.return_value.first.return_value = (
            TEST_ITEM
        )

        item = get_item(mock_db_session, str(TEST_ITEM_ID))

        mock_db_session.query.assert_called_once()
        mock_db_session.query.return_value.filter.assert_called_once()
        mock_db_session.query.return_value.filter.return_value.first.assert_called_once()

        assert item == TEST_ITEM

    def test_get_items(self, mock_db_session) -> None:
        mock_db_session.query.return_value.all.return_value = None

        items = get_items(mock_db_session)

        mock_db_session.query.assert_called_once()
        mock_db_session.query.return_value.all.assert_called_once()

        assert items == None
