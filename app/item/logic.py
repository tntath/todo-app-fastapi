from typing import List, Optional

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


def get_items(
    db: Session, completed: Optional[bool] = None, deleted: Optional[bool] = None
) -> List[ItemModel]:
    query = db.query(ItemModel)

    if completed is not None:
        query = query.filter(ItemModel.completed == completed)

    if deleted is not None:
        query = query.filter(ItemModel.deleted == deleted)

    return query.all()


def update_item(db: Session, item_id: str, item: ItemCreate) -> ItemModel | None:
    db_item = get_item(db, item_id)
    if db_item is None:
        return None
    for var, value in vars(item).items():
        setattr(db_item, var, value)
    db.commit()
    db.refresh(db_item)
    return db_item
