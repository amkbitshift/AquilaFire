import streamlit as st
from detect import detect_smoke
from risk import calculate_risk

st.title("🔥 AquilaFire – Wildfire Early Detection")

img = st.file_uploader("Upload Forest Image", type=["jpg", "png"])

temp = st.slider("Temperature (°C)", 20, 50, 35)
humidity = st.slider("Humidity (%)", 10, 90, 40)
wind = st.slider("Wind Speed (km/h)", 0, 20, 10)

if img:
    with open("temp.jpg", "wb") as f:
        f.write(img.read())

    smoke_conf = detect_smoke("temp.jpg")

    risk = calculate_risk(temp, humidity, wind, smoke_conf)

    st.metric("🔥 Fire Risk Score", f"{risk}/100")

    if smoke_conf > 0.6:
        st.error("Early Smoke Detected – Possible Wildfire")
    if risk > 70:
        st.error("HIGH FIRE RISK – Immediate Action Required")
    elif risk > 40:
        st.warning("MODERATE FIRE RISK")
    else:
        st.success("LOW FIRE RISK")
import matplotlib.pyplot as plt
from fire_spread import simulate_fire
import numpy as np

st.subheader("🔥 Fire Spread Simulation (Next Hours)")

grid = np.zeros((10, 10))
grid[5][5] = 1  # fire start point

wind = st.selectbox("Wind Direction", ["E", "W", "N", "S"])

for step in range(3):
    grid = simulate_fire(grid, wind)

fig, ax = plt.subplots()
ax.imshow(grid, cmap="hot")
ax.set_title("Predicted Fire Spread")
ax.axis("off")

st.pyplot(fig)
