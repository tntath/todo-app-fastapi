from fastapi import FastAPI

from app.item.router import router as item_router

description = """
## Description

This is a fully-featured CRUD API for maintaining a Todo list,
with additional options for listing completed and deleted items.

## Items

You will be able to:

* **Create** a new item
* **Read** an existing item
* **Update** an existing item
* **Delete/Remove** an existing item
* **List** all items
* **List** completed items
* **List** deleted items

"""

app = FastAPI(title="Todo List API", version="0.1.0", description=description)


app.include_router(item_router, tags=["items"])
