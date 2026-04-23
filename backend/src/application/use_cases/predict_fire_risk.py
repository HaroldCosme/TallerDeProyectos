from src.application.services.risk_classifier_service import classify_risk
from src.application.dtos.prediction_dto import PredictionDTO


def predict_fire_risk(data: dict):
    dto = PredictionDTO(**data)
    risk = classify_risk(dto)

    return {
        "nivel": risk
    }
