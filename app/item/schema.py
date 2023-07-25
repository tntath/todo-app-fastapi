from pydantic import BaseModel
from uuid import UUID


class ItemBase(BaseModel):
    title: str
    completed: bool = False
    deleted: bool = False


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: UUID

    class ConfigDict:
        from_attributes = True
