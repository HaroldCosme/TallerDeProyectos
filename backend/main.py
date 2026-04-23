from fastapi import FastAPI
from src.api.v1.routes import predictions, alerts, health

app = FastAPI()

app.include_router(predictions.router, prefix="/api")
app.include_router(alerts.router, prefix="/api")
app.include_router(health.router, prefix="/api")
