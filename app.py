import streamlit as st
import pandas as pd
import numpy as np
import time

# ---------------- Page Config ----------------
st.set_page_config(page_title="Solar AI Optimization", layout="wide")

st.title("⚡ AI Optimization Recommendations")
st.write("Actionable insights for energy savings and operational efficiency.")

# ---------------- Fake Data (replace with real later) ----------------
days = pd.date_range(start="2025-09-01", periods=15, freq="D")
energy = np.random.randint(5, 20, size=15)
water = np.random.randint(100, 300, size=15)

df = pd.DataFrame({
    "Date": days,
    "Energy (kWh)": energy,
    "Water (Liters)": water
}).set_index("Date")

# ---------------- Layout ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 High Priority")
    if st.button("🚨 Optimize Pump C-3 Schedule ($847/month)"):
        st.success("✅ Pump C-3 schedule optimization applied. Will take effect at 11 PM.")
    if st.button("🔶 Increase Solar Panel Angle (15% Efficiency)"):
        st.success("✅ Solar angle adjusted to 32° for autumn season.")

with col2:
    st.subheader("⚖️ Medium / Low Priority")
    if st.button("🔋 Battery Storage Optimization ($425/month)"):
        st.success("✅ Battery storage schedule implemented.")
    if st.button("🌱 Carbon Credit Maximization (+45 credits)"):
        st.success("✅ Carbon monitoring activated.")

st.divider()

# ---------------- Implementation Tracking ----------------
st.subheader("📈 Implementation Tracking")
implemented = np.random.randint(5, 12)
st.progress(implemented / 12)
st.write(f"Recommendations Implemented: {implemented}/12")
st.metric("Total Savings", "$2,847/month")
st.metric("ROI", "247%")

st.divider()

# ---------------- Graphs ----------------
st.subheader("📊 Energy & Water Trends")

tab1, tab2, tab3 = st.tabs(["Energy Trend", "Water Usage", "Comparison"])

with tab1:
    st.line_chart(df["Energy (kWh)"], height=300)

with tab2:
    st.area_chart(df["Water (Liters)"], height=300)

with tab3:
    st.bar_chart(df, height=300)

st.divider()

# ---------------- Billing Simulation ----------------
st.subheader("💰 Billing & Carbon Credits")
unit_rate = 5  # ₹ per kWh
billing = df["Energy (kWh)"].sum() * unit_rate
carbon_saving = df["Energy (kWh)"].sum() * 0.8

st.write(f"**Estimated Bill:** ₹{billing:.2f}")
st.write(f"**Carbon Credits Saved:** {carbon_saving:.2f} kg CO₂")
