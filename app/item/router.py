from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.session import get_db

from .logic import create_item, get_item, get_items, remove_item, update_item
from .model import Item as ItemModel
from .schema import Item, ItemCreate

router = APIRouter()


@router.post("/items/", response_model=Item, summary="Create a new item.")
def create_single_item(item: ItemCreate, db: Session = Depends(get_db)) -> ItemModel:
    """
    Create a new item in the system.

    Parameters
    ----------

    **item** : ItemCreate(title: string, completed: Boolean, deleted: Boolean)


    Returns
    -------
    Item(id: UUID, title: string, completed: Boolean, deleted: Boolean)
    """
    return create_item(db, item)


@router.get("/items/{item_id}", response_model=Item, summary="Get a single item.")
def get_single_item(item_id: str, db: Session = Depends(get_db)) -> ItemModel:
    """
    Get a single item from the system.

    Parameters
    ----------
    **item_id**: UUID

    Returns
    -------
    Item(id: UUID, title: string, completed: Boolean, deleted: Boolean)
    """
    item = get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/items/", response_model=List[Item], summary="Get all items.")
def get_all_items(
    db: Session = Depends(get_db),
    completed: Optional[bool] = None,
    deleted: Optional[bool] = None,
) -> List[ItemModel]:
    """
    Get all items from the system.

    Query parameters
    ----------
    **completed**: Boolean

    **deleted**: Boolean

    Returns
    -------
    **List[Item]**

    where:
     Item(id: UUID, title: string, completed: Boolean, deleted: Boolean)
    """
    return get_items(db, completed=completed, deleted=deleted)


@router.put("/items/{item_id}", response_model=Item, summary="Update a single item.")
def update_single_item(
    item_id: str, item: ItemCreate, db: Session = Depends(get_db)
) -> ItemModel:
    """
    Update a single item in the system.

    Parameters
    ----------
    **item_id**: UUID

    **item**: ItemCreate(title: string, completed: Boolean, deleted: Boolean)

    Returns
    -------
    Item (id: UUID, title: string, completed: Boolean, deleted: Boolean)

    """
    updated_item = update_item(db, item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@router.delete("/items/{item_id}", response_model=Item, summary="Delete a single item.")
def remove_single_item(item_id: str, db: Session = Depends(get_db)) -> ItemModel:
    """
    Delete a single item from the system.

    Parameters
    ----------
    **item_id**: UUID

    Returns
    -------
    Item (id: UUID, title: string, completed: Boolean, deleted: Boolean)
    """
    deleted_item = remove_item(db, item_id)
    if deleted_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return deleted_item
