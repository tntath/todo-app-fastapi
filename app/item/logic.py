from typing import List

from sqlalchemy.orm import Session

from .model import Item as ItemModel
from .schema import ItemCreate


def create_item(db: Session, item: ItemCreate) -> ItemModel:
    db_item = ItemModel(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: str) -> ItemModel | None:
    return db.query(ItemModel).filter(ItemModel.id == item_id).first()


def get_items(db: Session) -> List[ItemModel]:
    return db.query(ItemModel).all()