import time

from fastapi import APIRouter
from loguru import logger

from app.exceptions.custom import ClientError, ServerError
from app.schemas.perspective import RequestImageB64, ResponseImageB64
from app.services.perspective import PerspectiveCorrectionService
from app.utils.conversions import b64_to_np

perspective_router = APIRouter()


@perspective_router.post("/perspective-correction",
                         response_model=ResponseImageB64,
                         summary=("Extracts the images borders"),
                         description=("This route uses the coordinate points (x, y)"
                                      "of the object and applies a perspective correction."))
async def perspective_correction(request: RequestImageB64):
    start_time = time.time()

    image_np = b64_to_np(request.image_b64)
    if image_np is None:
        raise ClientError

    service = PerspectiveCorrectionService()
    image_b64 = service.fix_perspective(image_np, request.points)
    if image_b64 is None:
        raise ServerError

    response = ResponseImageB64(image_b64=image_b64)
    latency = time.time() - start_time
    logger.info(f"[+] Response: {response.image_b64[:10]}... | Latency: {latency} s")
    return response
