import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml_model",   # change this to "ml" if folder is named ml
    "models",
    "emission_models.pkl"
)

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

models = joblib.load(MODEL_PATH)

def predict_emission(vehicle_type, years_ahead):
    model = models[vehicle_type]

    last_year = 2020
    future_years = np.arange(
        last_year + 1,
        last_year + years_ahead + 1
    ).reshape(-1, 1)

    predictions = model.predict(future_years)
    return future_years.flatten(), predictions
