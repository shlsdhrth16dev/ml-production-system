import joblib
from fastapi import FastAPI

from src.services.schemas import PredictionRequest
from src.services.feature_adapter import build_features_from_request
from src.utils.logger import get_logger

logger = get_logger()

app = FastAPI(title="ML Inference Service")

# Load model ONCE at startup
model = joblib.load("models/baseline_model.joblib")
logger.info("Model loaded successfully")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictionRequest):
    features = build_features_from_request(request.model_dump())
    prediction = model.predict(features)[0]

    return {
        "prediction": int(prediction)
    }
