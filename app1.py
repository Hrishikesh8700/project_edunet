import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from calculator import RoadTransport, Ship, Airplane

st.set_page_config(
    page_title="Fuel & Emission Dashboard",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("🚘✈️🚢 Fuel Consumption & Emission Dashboard")
st.markdown("""
An interactive system to analyze **fuel usage and CO₂ emissions**
across **Road Transport, Shipping, and Aviation**.
""")

# ---------------- SIDEBAR ----------------
st.sidebar.header("📌 Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Calculator", "Vehicle Comparison", "General Trends", "Insights & About"]
)

# ---------------- CALCULATOR ----------------
if section == "Calculator":
    st.subheader("🔢 Fuel & Emission Calculator")

    col1, col2, col3 = st.columns(3)

    with col1:
        vehicle_type = st.selectbox(
            "Vehicle Type",
            ["Road Transport", "Ship", "Airplane"]
        )

    with col2:
        distance = st.number_input("Distance (km)", min_value=1.0)

    with col3:
        engine_size = st.number_input("Engine Size / Capacity", min_value=0.1)

    if st.button("Calculate"):
        if vehicle_type == "Road Transport":
            vehicle = RoadTransport(distance, engine_size)
        elif vehicle_type == "Ship":
            vehicle = Ship(distance, engine_size)
        else:
            vehicle = Airplane(distance, engine_size)

        fuel = vehicle.fuel_consumption()
        co2 = vehicle.co2_emission()

        st.success("Calculation Completed")

        m1, m2, m3 = st.columns(3)
        m1.metric("Fuel Used (Liters)", f"{fuel:.2f}")
        m2.metric("CO₂ Emission (kg)", f"{co2:.2f}")
        m3.metric("CO₂ per km", f"{co2/distance:.2f}")

        fig, ax = plt.subplots()
        ax.bar(["Fuel", "CO₂"], [fuel, co2])
        ax.set_title("Fuel vs CO₂")
        st.pyplot(fig)

# ---------------- COMPARISON ----------------
elif section == "Vehicle Comparison":
    st.subheader("📊 Vehicle Comparison (Same Distance)")

    distance = st.slider("Select Distance (km)", 50, 2000, 500)
    engine = st.slider("Engine Size", 0.5, 5.0, 2.0)

    vehicles = {
        "Road": RoadTransport(distance, engine),
        "Ship": Ship(distance, engine),
        "Airplane": Airplane(distance, engine)
    }

    fuel_values = [v.fuel_consumption() for v in vehicles.values()]
    co2_values = [v.co2_emission() for v in vehicles.values()]

    fig, ax = plt.subplots()
    ax.bar(vehicles.keys(), fuel_values)
    ax.set_ylabel("Fuel (Liters)")
    ax.set_title("Fuel Consumption Comparison")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.bar(vehicles.keys(), co2_values)
    ax.set_ylabel("CO₂ (kg)")
    ax.set_title("CO₂ Emission Comparison")
    st.pyplot(fig)

# ---------------- GENERAL TRENDS ----------------
elif section == "General Trends":
    st.subheader("🌍 Historical Transport Emission Trends")

    df = pd.read_csv("data/transport_emissions.csv")
    st.dataframe(df)

    fig, ax = plt.subplots()
    ax.plot(df["Year"], df["Road"], label="Road")
    ax.plot(df["Year"], df["Ship"], label="Ship")
    ax.plot(df["Year"], df["Airplane"], label="Airplane")

    ax.set_xlabel("Year")
    ax.set_ylabel("Emission Index")
    ax.set_title("Past Fuel / CO₂ Trends")
    ax.legend()
    st.pyplot(fig)

    st.info("This analysis is based on historical transport emission data (no prediction).")

# ---------------- ABOUT ----------------
else:
    st.subheader("ℹ️ Project Insights & About")

    st.markdown("""
### 🔹 Key Observations
- Aviation shows the fastest emission growth
- Shipping is fuel-intensive but efficient per ton
- Road transport contributes consistently over time

### 🔹 Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib
- OOP Concepts

### 🔹 Academic Value
- Real-world problem
- Clean architecture
- Interactive analytics
- Extendable to ML in future
""")
