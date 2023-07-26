from fastapi import FastAPI

from app.item.router import router as item_router

app = FastAPI(title="FastAPI, Docker, and Traefik")


app.include_router(item_router, tags=["items"])
