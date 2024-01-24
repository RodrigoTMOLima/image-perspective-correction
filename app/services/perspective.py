from typing import List

import cv2
import numpy as np
from loguru import logger

from app.utils.conversions import np_to_b64


class PerspectiveCorrectionService:
    def __init__(self) -> None:
        pass

    def fix_perspective(self, image_np: np.ndarray, points: List[List[int]]) -> str:
        try:
            warp_np = self._fix(image_np, points)
            image_b64 = np_to_b64(warp_np)
        except Exception as e:
            image_b64 = None
            logger.error(f"[-] Error applying perspective correction: {e}")
        return image_b64

    def _get_euclid_distance(self, pt1: List[int], pt2: List[int]) -> np.ndarray:
        """L2"""
        return np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

    def _fix(self, img_np: np.ndarray, points: List[List[int]]) -> np.ndarray:
        """
        Points in counter-clockwise order, starting from top left

        Point A: Upper left corner
        Point B: Bottom left corner
        Point C: Bottom right corner
        Point D: Upper right corner
        """
        width_ad = self._get_euclid_distance(points[0], points[3])
        width_bc = self._get_euclid_distance(points[1], points[2])
        max_width = max(int(width_ad), int(width_bc))

        height_ab = self._get_euclid_distance(points[0], points[1])
        height_cd = self._get_euclid_distance(points[2], points[3])
        max_height = max(int(height_ab), int(height_cd))

        src_pts = np.array(points, dtype=np.float32)
        dst_pts = np.array([[0, 0],
                            [0, max_height - 1],
                            [max_width - 1, max_height - 1],
                            [max_width - 1, 0]], dtype=np.float32)

        p_transform = cv2.getPerspectiveTransform(src_pts, dst_pts)
        warp_np = cv2.warpPerspective(src=img_np,
                                      M=p_transform,
                                      dsize=(max_width, max_height),
                                      flags=cv2.INTER_LINEAR)
        return warp_np
