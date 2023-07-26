from uuid import UUID

from pydantic import BaseModel


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
