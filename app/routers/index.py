from fastapi import APIRouter

index_router = APIRouter()


@index_router.get("/")
def index():
    return "Welcome to the Image Border Extraction API. Access /docs for more info."
