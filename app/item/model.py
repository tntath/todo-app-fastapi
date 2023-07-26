from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text

from database.base import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=text("(gen_random_uuid())"),
    )
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)
