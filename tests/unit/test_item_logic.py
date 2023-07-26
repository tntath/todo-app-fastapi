import uuid
from unittest.mock import patch, Mock

import pytest

from app.item.logic import create_item, get_item, get_items, update_item, remove_item
from app.item.schema import Item, ItemCreate
from app.item.model import Item as ItemModel

TEST_ITEM_ID = uuid.uuid4()
TEST_ITEM = Item(id=TEST_ITEM_ID, title="Test Item", completed=True, deleted=True)
TEST_ITEM_MODEL = ItemModel(**TEST_ITEM.model_dump())


@pytest.fixture
@patch("app.item.logic.Session")
def mock_db_session(session) -> Mock:
    return session


@pytest.fixture
def mock_query(mock_db_session) -> Mock:
    return mock_db_session.query.return_value


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

    def test_get_items_completed(self, mock_db_session, mock_query) -> None:
        mock_query.filter.return_value = mock_query
        mock_query.all.return_value = []

        items = get_items(mock_db_session, completed=True)

        assert mock_query.filter.call_args.args[0].compare(ItemModel.completed == True)
        mock_query.all.assert_called_once()
        assert items == []

    def test_get_items_deleted(self, mock_db_session, mock_query) -> None:
        mock_query.filter.return_value = mock_query
        mock_query.all.return_value = []

        items = get_items(mock_db_session, deleted=True)

        assert mock_query.filter.call_args.args[0].compare(ItemModel.deleted == True)
        mock_query.all.assert_called_once()
        assert items == []

    def test_update_item(self, mock_db_session):
        mock_db_session.query.return_value.filter.return_value.first.return_value = (
            TEST_ITEM
        )

        item = update_item(
            mock_db_session,
            str(TEST_ITEM_ID),
            ItemCreate(title="Test Item", completed=False, deleted=False),
        )

        mock_db_session.query.assert_called_once()
        mock_db_session.commit.assert_called_once()
        mock_db_session.refresh.assert_called_once()

        assert item == TEST_ITEM

    def test_remove_item(self, mock_db_session):
        mock_db_session.query.return_value.filter.return_value.first.return_value = (
            TEST_ITEM
        )

        item = remove_item(mock_db_session, str(TEST_ITEM_ID))

        mock_db_session.query.assert_called_once()
        mock_db_session.delete.assert_called_once()
        mock_db_session.commit.assert_called_once()

        assert item == TEST_ITEM
