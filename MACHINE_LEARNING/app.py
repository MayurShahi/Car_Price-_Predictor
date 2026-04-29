from fastapi import FastAPI
from pydantic import BaseModel
import joblib, numpy as np, pandas as pd

app = FastAPI(title="Car Price Predictor")

model = joblib.load("car_price_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

class CarInput(BaseModel):
    brand: str
    model: str
    model_year: int
    milage: float
    fuel_type: str
    transmission: str
    ext_col: str
    int_col: str
    clean_title: str       # "Yes" / "UNKNOWN"
    Accident_occured: str  # "YES" / "NO"
    Engine_capacity: float
    Horse_Power: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(car: CarInput):
    df = pd.DataFrame([car.dict()])
    processed = preprocessor.transform(df)
    log_price = model.predict(processed)[0]
    price = float(np.expm1(log_price))  # remove if you didn't log-transform
    return {
        "predicted_price_usd": round(price, 2),
        "input_received": car.dict()
    }