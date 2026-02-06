import streamlit as st
import matplotlib.pyplot as plt
from calculator import RoadTransport, Ship, Airplane

st.set_page_config(page_title="Fuel & Emission Calculator")

st.title("🚘✈️🚢 Fuel Consumption & CO₂ Emission Calculator")

vehicle_type = st.selectbox(
    "Select Vehicle Type",
    ["Road Transport", "Ship", "Airplane"]
)

distance = st.number_input("Distance (km)", min_value=1.0)
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

    st.success("Calculation Completed ✅")
    st.metric("Fuel Used (Liters)", f"{fuel:.2f}")
    st.metric("CO₂ Emission (kg)", f"{co2:.2f}")

    fig, ax = plt.subplots()
    ax.bar(["Fuel", "CO₂"], [fuel, co2])
    st.pyplot(fig)
