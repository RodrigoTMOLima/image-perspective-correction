from typing import List

from pydantic import BaseModel


class RequestImageB64(BaseModel):
    image_b64: str
    points: List[List[int]]  # Four x, y pairs

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "image_b64": ("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCA"
                                  "IAAACQd1PeAAAAAXNSR0IArs4c6QAAAARnQ"
                                  "U1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7D"
                                  "AcdvqGQAAAAMSURBVBhXY2BgYAAAAAQAAVz"
                                  "N/2kAAAAASUVORK5CYII="),
                    "points": [
                        [20, 30],  # Top left
                        [30, 70],  # Bottom left
                        [50, 65],  # Bottom right
                        [40, 10],  # Top right
                    ]
                }
            ]
        }
    }


class ResponseImageB64(BaseModel):
    image_b64: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "image_b64": ("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCA"
                                  "IAAACQd1PeAAAAAXNSR0IArs4c6QAAAARnQ"
                                  "U1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7D"
                                  "AcdvqGQAAAAMSURBVBhXY2BgYAAAAAQAAVz"
                                  "N/2kAAAAASUVORK5CYII=")
                }
            ]
        }
    }
