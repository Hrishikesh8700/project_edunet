import streamlit as st
import pandas as pd
import plotly.express as px
from calculator import RoadTransport, Ship, Airplane
from ml_model.predictor import predict_emission

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Fuel & Emission Analytics",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("🚘✈️🚢 Fuel Consumption & Emission Analytics Dashboard")
st.markdown(
    "Modern interactive dashboard to analyze fuel usage and CO₂ emissions "
    "across **Road Transport, Shipping, and Aviation**."
)

# ---------------- SIDEBAR ----------------
st.sidebar.header("📌 Navigation")
section = st.sidebar.radio(
    "Select Section",
    ["Calculator", "Vehicle Comparison", "General Trends", "About"]
)

# =====================================================
# 🔢 CALCULATOR TAB
# =====================================================
if section == "Calculator":
    st.subheader("🔢 Fuel & CO₂ Calculator")

    col1, col2, col3 = st.columns(3)
    with col1:
        vehicle_type = st.selectbox(
            "Vehicle Type",
            ["Road Transport", "Ship", "Airplane"]
        )
    with col2:
        distance = st.number_input("Distance (km)", min_value=1.0, value=500.0)
    with col3:
        engine_size = st.number_input("Engine Size / Capacity", min_value=0.1, value=2.0)

    if st.button("Calculate"):
        if vehicle_type == "Road Transport":
            vehicle = RoadTransport(distance, engine_size)
        elif vehicle_type == "Ship":
            vehicle = Ship(distance, engine_size)
        else:
            vehicle = Airplane(distance, engine_size)

        fuel = vehicle.fuel_consumption()
        co2 = vehicle.co2_emission()
        co2_per_km = co2 / distance

        m1, m2, m3 = st.columns(3)
        m1.metric("Fuel Used (Liters)", f"{fuel:.2f}")
        m2.metric("CO₂ Emission (kg)", f"{co2:.2f}")
        m3.metric("CO₂ per km", f"{co2_per_km:.2f}")

        df_calc = pd.DataFrame({
            "Metric": ["Fuel (Liters)", "CO₂ (kg)"],
            "Value": [fuel, co2]
        })

        fig = px.bar(
            df_calc,
            x="Metric",
            y="Value",
            color="Metric",
            text_auto=True,
            title="Fuel vs CO₂ Emission"
        )
        st.plotly_chart(fig, use_container_width=True)

# =====================================================
# 📊 VEHICLE COMPARISON TAB
# =====================================================
elif section == "Vehicle Comparison":
    st.subheader("📊 Vehicle Comparison (Same Distance)")

    distance = st.slider("Distance (km)", 100, 3000, 1000)
    engine_size = st.slider("Engine Size / Capacity", 0.5, 6.0, 2.0)

    vehicles = {
        "Road": RoadTransport(distance, engine_size),
        "Ship": Ship(distance, engine_size),
        "Airplane": Airplane(distance, engine_size)
    }

    df_compare = pd.DataFrame({
        "Vehicle": vehicles.keys(),
        "Fuel (Liters)": [v.fuel_consumption() for v in vehicles.values()],
        "CO₂ (kg)": [v.co2_emission() for v in vehicles.values()]
    })

    fig = px.bar(
        df_compare,
        x="Vehicle",
        y=["Fuel (Liters)", "CO₂ (kg)"],
        barmode="group",
        title="Fuel & CO₂ Comparison Across Transport Modes"
    )
    st.plotly_chart(fig, use_container_width=True)
'''
# =====================================================
# 🌍 GENERAL TRENDS TAB
# =====================================================
elif section == "General Trends":
    st.subheader("🌍 Historical Transport Emission Trends")

    df = pd.read_csv(r"C:\Users\hrishikesh mhaske'\OneDrive\Desktop\fuel_emmsion\data")
    st.dataframe(df)

    df_long = df.melt(
        id_vars="Year",
        value_vars=["Road", "Ship", "Airplane"],
        var_name="Transport Mode",
        value_name="Emission Index"
    )

    fig = px.line(
        df_long,
        x="Year",
        y="Emission Index",
        color="Transport Mode",
        markers=True,
        title="Past Fuel / CO₂ Emission Trends"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info("This section visualizes historical data only (no prediction or ML).")



elif section == "ML Prediction":
    st.subheader("🤖 ML-Based Future Emission Prediction")

    vehicle = st.selectbox(
        "Select Vehicle Type",
        ["Road", "Ship", "Airplane"]
    )

    years = st.slider(
        "Years into the future",
        1, 20, 5
    )

    future_years, predictions = predict_emission(vehicle, years)

    df_pred = pd.DataFrame({
        "Year": future_years,
        "Predicted Emission": predictions
    })

    st.dataframe(df_pred)

    fig = px.line(
        df_pred,
        x="Year",
        y="Predicted Emission",
        markers=True,
        title=f"Predicted Emissions for {vehicle}"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "Prediction generated using a pre-trained Linear Regression model "
        "based on historical Kaggle transport emission data."
    )
'''
# =====================================================
# ℹ️ ABOUT TAB
# =====================================================
else:
    st.subheader("ℹ️ About This Project")

    st.markdown("""
### 🔹 Project Overview
This project analyzes fuel consumption and CO₂ emissions for:
- Road Transport
- Shipping
- Aviation

### 🔹 Features
- Interactive Streamlit UI
- Object-Oriented backend design
- Modern Plotly visualizations
- Real-world dataset integration

### 🔹 Technologies Used
- Python
- Streamlit
- Pandas
- Plotly

### 🔹 Academic Value
- Clean architecture
- Environment-focused analytics
- Extendable for ML-based prediction
""")
    
