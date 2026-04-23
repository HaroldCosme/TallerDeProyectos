from pydantic import BaseModel

class AlertResponse(BaseModel):
    nivel: str
    mensaje: str
