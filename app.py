import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Solar Pump Dashboard", layout="wide")

st.title("⚡ Solar Pump Dashboard")

# --- Fake Data (replace later with real sensor data) ---
days = pd.date_range(start="2025-01-01", periods=15, freq="D")
energy = np.random.randint(5, 20, size=15)   # kWh
water = np.random.randint(100, 300, size=15) # Liters

df = pd.DataFrame({
    "Date": days,
    "Energy (kWh)": energy,
    "Water (Liters)": water
}).set_index("Date")

# --- KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Energy", f"{df['Energy (kWh)'].sum()} kWh")
col2.metric("Total Water Pumped", f"{df['Water (Liters)'].sum()} L")
col3.metric("Avg Energy/Day", f"{df['Energy (kWh)'].mean():.2f} kWh")

st.divider()

# --- Graphs ---
st.subheader("📊 Energy & Water Trends")

tab1, tab2, tab3 = st.tabs(["Energy Trend", "Water Usage", "Comparison"])

with tab1:
    st.line_chart(df["Energy (kWh)"], height=300)

with tab2:
    st.area_chart(df["Water (Liters)"], height=300)

with tab3:
    st.bar_chart(df, height=300)

st.divider()

# --- Billing Simulation ---
st.subheader("💰 Billing & Carbon Credits")

unit_rate = 5  # ₹ per kWh
billing = df["Energy (kWh)"].sum() * unit_rate
carbon_saving = df["Energy (kWh)"].sum() * 0.8  # assume 0.8kg CO₂ saved per kWh

st.write(f"**Estimated Bill:** ₹{billing:.2f}")
st.write(f"**Carbon Credits Saved:** {carbon_saving:.2f} kg CO₂")

st.success("✅ Dashboard ready. Graphs & metrics working smoothly!")
