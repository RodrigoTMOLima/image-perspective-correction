import uvicorn
from fastapi import FastAPI

from app import __version__
from app.routers.index import index_router
from app.routers.perspective import perspective_router

app = FastAPI(
    title="Image Perspective Correction API",
    summary="Applies a perspective correction on the image",
    description="",
    version=__version__
)
app.include_router(perspective_router)
app.include_router(index_router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")
