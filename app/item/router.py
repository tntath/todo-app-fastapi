from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db

from .logic import create_item
from .schema import Item, ItemCreate
from .model import Item as ItemModel

router = APIRouter()


@router.post("/items/", response_model=Item)
def create_single_item(item: ItemCreate, db: Session = Depends(get_db)) -> ItemModel:
    return create_item(db, item)
