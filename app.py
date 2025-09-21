import streamlit as st
import pandas as pd
import numpy as np

# Page title etc.
st.title("Solar & Optimization Analytics")
st.write("AI-driven energy insights and actionable recommendations")

# Last updated timestamp
st.caption(f"Last updated: {pd.Timestamp.now().strftime('%B %d, %Y at %I:%M %p')}")

# --- Metrics row ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("kWh Today", "1,024", "+12%")
m2.metric("kWh Used", "780", "-5%")
m3.metric("Credits This Month", "142", "+20%")
m4.metric("Savings This Month", "$2,350", "+18%")

st.divider()

# --- Filters and Export / Refresh Buttons ---
f1, f2, f3 = st.columns([2,2,1])
with f1:
    time_period = st.selectbox("Time Period", ["Last 7 Days", "Last 30 Days", "Year to Date"])
with f2:
    chart_type = st.selectbox("Chart Type", ["Line Chart", "Area Chart", "Bar Chart"])
with f3:
    if st.button("🔁 Refresh Data"):
        st.success("Data refreshed!")
    st.download_button("⬇ Export Data", data="dummy_data", file_name="solar_data.csv")

st.divider()

# --- Graphs ---
# Sample data generation
days = pd.date_range(end=pd.Timestamp.now(), periods=14)
solar_gen = np.random.randint(200, 500, size=14)
grid_use = np.random.randint(100, 300, size=14)
pump_eff = np.random.uniform(70, 95, size=14)

df1 = pd.DataFrame({
    "Date": days,
    "Solar Generation": solar_gen,
    "Grid Consumption": grid_use
}).set_index("Date")

df2 = pd.DataFrame({
    "Date": days,
    "Pump A-1": pump_eff,
    "Pump B-2": pump_eff - 5,
    "Pump C-3": pump_eff - 10
}).set_index("Date")

st.subheader("Solar Output vs Grid Consumption")
if chart_type == "Line Chart":
    st.line_chart(df1)
elif chart_type == "Area Chart":
    st.area_chart(df1)
else:
    st.bar_chart(df1)

st.subheader("Pump Efficiency Trends")
st.line_chart(df2)

st.divider()

# --- Recommendations with Action Buttons ---
st.subheader("AI Recommendations")

# maintain state to show implemented or not
if "impl" not in st.session_state:
    st.session_state.impl = {
        "opt_pump": False,
        "angle": False,
        "battery": False,
        "carbon": False
    }

# High Priority items
hp1, hp2 = st.columns(2)
with hp1:
    st.markdown("**Optimize Pump C-3 Schedule**  \nPotential savings: $847/month", unsafe_allow_html=True)
    if not st.session_state.impl["opt_pump"]:
        if st.button("Implement Pump C-3"):
            st.session_state.impl["opt_pump"] = True
            st.success("✅ Pump C-3 schedule optimization implemented.")
    else:
        st.info("✅ Pump C-3 optimization already implemented")

with hp2:
    st.markdown("**Increase Solar Panel Angle**  \nExpected gain: 15% efficiency", unsafe_allow_html=True)
    if not st.session_state.impl["angle"]:
        if st.button("Implement Angle Change"):
            st.session_state.impl["angle"] = True
            st.success("✅ Solar panel angle changed to optimal position.")
    else:
        st.info("✅ Solar panel angle already optimal")

# Medium Priority
mp1, mp2 = st.columns(2)
with mp1:
    st.markdown("**Battery Storage Optimization**  \nPotential savings: $425/month", unsafe_allow_html=True)
    if not st.session_state.impl["battery"]:
        if st.button("Implement Battery Optimization"):
            st.session_state.impl["battery"] = True
            st.success("✅ Battery storage optimization applied.")
    else:
        st.info("✅ Battery optimization already done")
with mp2:
    st.markdown("**Carbon Credit Maximization**  \nAdditional credits: 45/month", unsafe_allow_html=True)
    if not st.session_state.impl["carbon"]:
        if st.button("Implement Carbon Credits"):
            st.session_state.impl["carbon"] = True
            st.success("✅ Carbon credits program enabled.")
    else:
        st.info("✅ Carbon credit program already enabled")

st.divider()

# --- Implementation Tracking ---
st.subheader("Implementation Tracking")
total = len(st.session_state.impl)
done = sum(1 for v in st.session_state.impl.values() if v)
st.progress(done / total)
st.write(f"Recommendations Implemented: {done}/{total}")
# Example savings calculation
savings = done * 500  # assume each implementation gives ~$500 saving for demo
st.metric("Estimated Monthly Savings", f"${savings}")
st.metric("Estimated ROI", f"{done * 10}%")  # dummy ROI

