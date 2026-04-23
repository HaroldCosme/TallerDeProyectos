from fastapi import APIRouter
from src.application.use_cases.predict_fire_risk import predict_fire_risk


router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    result = predict_fire_risk(data)
    return result
