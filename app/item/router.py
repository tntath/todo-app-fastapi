from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.session import get_db

from .logic import create_item, get_item, get_items, update_item
from .model import Item as ItemModel
from .schema import Item, ItemCreate

router = APIRouter()


@router.post("/items/", response_model=Item)
def create_single_item(item: ItemCreate, db: Session = Depends(get_db)) -> ItemModel:
    return create_item(db, item)


@router.get("/items/{item_id}", response_model=Item)
def get_single_item(item_id: str, db: Session = Depends(get_db)) -> ItemModel:
    item = get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/items/", response_model=List[Item])
def get_all_items(
    db: Session = Depends(get_db),
    completed: Optional[bool] = None,
    deleted: Optional[bool] = None,
) -> List[ItemModel]:
    return get_items(db, completed=completed, deleted=deleted)


@router.put("/items/{item_id}", response_model=Item)
def update_single_item(
    item_id: str, item: ItemCreate, db: Session = Depends(get_db)
) -> ItemModel:
    updated_item = update_item(db, item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item
