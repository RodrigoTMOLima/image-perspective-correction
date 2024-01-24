import base64
from io import BytesIO

import cv2
import numpy as np
from loguru import logger
from PIL import Image


def b64_to_pil(image_b64: str) -> Image.Image:
    """Converts an image encoded as a Base64 string into a Pillow Image object"""
    try:
        image_pil = Image.open(BytesIO(base64.b64decode(image_b64)))
        logger.info(f"[*] Image B64 converted to PIL Image of size: {image_pil.size}")
    except Exception as e:
        image_pil = None
        logger.error(f"[-] Error converting B64 to PIL: {e}")
    return image_pil


def pil_to_b64(image_pil: Image.Image) -> str:
    """Converts a Pillow Image object into an image represented as a Base64-encoded string."""
    try:
        buf = BytesIO()
        image_pil.save(buf, format="PNG")
        image_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        logger.info(f"[*] Image PIL of size {image_pil.size} converted to Base64-encoded string")
    except Exception as e:
        image_b64 = None
        logger.error(f"[-] Error converting PIL to B64: {e}")
    return image_b64


def b64_to_np(image_b64: str) -> np.ndarray:
    """Converts an image encoded as a Base64 string into a NumPy array in OpenCV BGR format."""
    try:
        image_np = np.fromstring(base64.b64decode(image_b64), np.uint8)
        image_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        logger.info(f"[*] Image B64 converted to CV image of size: {image_np.size}")
    except Exception as e:
        image_np = None
        logger.error(f"[-] Error converting B64 to NumPy array: {e}")
    return image_np


def np_to_b64(image_np: np.ndarray) -> str:
    """
    Converts a NumPy array in OpenCV BGR format into
    an image represented as a Base64-encoded string.
    """
    try:
        _, buf = cv2.imencode('.png', image_np)
        image_b64 = base64.b64encode(buf).decode("utf-8")
        logger.info(f"[*] CV image of size {image_np.shape} converted to Base64-encoded string")
    except Exception as e:
        image_b64 = None
        logger.error(f"[-] Error converting NumPy array to B64: {e}")
    return image_b64
