from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI(
    title="NYC Taxi Trip Duration Prediction API",
    description="Predict taxi trip duration using a Random Forest model trained on the NYC Taxi dataset.",
    version="1.0.0"
)

# Load model
model = joblib.load("taxi_trip_duration_model.pkl")
columns = joblib.load("feature_columns.pkl")

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Taxi Trip Duration Prediction API"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }

# Input schema
class TaxiTrip(BaseModel):
    pickup_longitude: float
    pickup_latitude: float
    dropoff_longitude: float
    dropoff_latitude: float
    pickup_hour: int
    pickup_day: int
    pickup_month: int
    pickup_weekday: int
    is_weekend: int
    distance: float
    is_peak_hour: int
    time_of_day_Morning: int
    time_of_day_Night: int

# Prediction endpoint
@app.post("/predict")
def predict(trip: TaxiTrip):
    input_df = pd.DataFrame([trip.model_dump()])
    input_df = input_df[columns]

    prediction_log = model.predict(input_df)[0]
    prediction = np.expm1(prediction_log)

    return {
    "status": "success",
    "prediction": {
        "trip_duration_seconds": round(float(prediction),2),
        "trip_duration_minutes": round(float(prediction)/60,2)
    },
    "model": "Random Forest Regressor",
    "version": "1.0.0"
}