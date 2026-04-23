from pydantic import BaseModel

class PredictionRequest(BaseModel):
    temperatura: float
    humedad: float
    viento: float
    ndvi: float
