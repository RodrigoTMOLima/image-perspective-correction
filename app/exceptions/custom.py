from typing import Any, Dict, Optional

from fastapi import HTTPException


class ServerError(HTTPException):
    def __init__(self,
                 status_code: int = 500,
                 detail: Any = "SERVER ERROR",
                 headers: Optional[Dict[str, str]] = None) -> None:
        super().__init__(status_code, detail, headers)


class ClientError(HTTPException):
    def __init__(self,
                 status_code: int = 400,
                 detail: Any = "CLIENT ERROR",
                 headers: Optional[Dict[str, str]] = None) -> None:
        super().__init__(status_code, detail, headers)
