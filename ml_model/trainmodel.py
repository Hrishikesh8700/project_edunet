import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load dataset
df = pd.read_csv(r"C:\Users\hrishikesh mhaske'\OneDrive\Desktop\fuel_emmsion\data\transport_emissions_ml.csv")


models = {}

# Train separate model for each vehicle
for vehicle in df["Vehicle"].unique():
    vehicle_df = df[df["Vehicle"] == vehicle]

    X = vehicle_df[["Year"]]
    y = vehicle_df["Emission"]

    model = LinearRegression()
    model.fit(X, y)

    models[vehicle] = model

# Save models
os.makedirs("models", exist_ok=True)
joblib.dump(models, "models/emission_models.pkl")

print("✅ Models trained and saved successfully")
