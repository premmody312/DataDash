import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from growthbook import GrowthBook

# Configure Streamlit app
st.set_page_config(page_title="Real-Time Analytics Dashboard", layout="wide")

# Generate Dummy Data
@st.cache_data
def get_dummy_data():
    timestamps = pd.date_range(start="2024-01-01", periods=60, freq="s")
    return pd.DataFrame({
        "timestamp": timestamps,
        "page_views": np.random.randint(50, 500, size=len(timestamps)),
        "user_sessions": np.random.randint(10, 50, size=len(timestamps)),
        "conversion_rate": np.random.uniform(1, 5, size=len(timestamps)),
    })

# Dummy data for simulation
data = get_dummy_data()

# Initialize GrowthBook
gb = GrowthBook()
gb.set_features({"new_feature": {"defaultValue": True}})

# Page Title
st.markdown("<h1 style='text-align: center; color: white;'>Real-Time Analytics Dashboard (Simulation)</h1>", unsafe_allow_html=True)

# Create Columns for Layout
col1, col2 = st.columns([2, 1])  # 2:1 ratio for main chart and side data

# ---- Titles and Containers ----
with col1:
    st.markdown("<h2 style='text-align: left; color: white;'>Real-Time Traffic Data</h2>", unsafe_allow_html=True)
    chart_placeholder = st.empty()  # Placeholder for real-time chart

# Create containers in col2
with col2:
    with st.container():
        st.markdown("<h3 style='text-align: left; color: white;'>Simulated Google Analytics Data</h3>", unsafe_allow_html=True)
        placeholder_ga = st.empty()
    with st.container():
        st.markdown("<h3 style='text-align: left; color: white;'>Simulated LogRocket Interaction Logs </h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: left; color: white;'>(Most Recent 5 User Interaction Logs)</h5>", unsafe_allow_html=True)
        placeholder_logrocket = st.empty()
    with st.container():
        st.markdown("<h3 style='text-align: left; color: white;'>Simulated GrowthBook A/B Testing Results</h3>", unsafe_allow_html=True)
        placeholder_growthbook = st.empty()

# Initialize LogRocket Logs
log_rocket_logs = []

# Real-Time Simulation Loop
for i in range(1, len(data)):
    # Update data dynamically
    current_data = data.iloc[:i]

    # ---- Update Real-Time Chart ----
    with col1:
        fig, ax = plt.subplots(figsize=(12, 6))  # Set height and width for the chart
        ax.plot(current_data["timestamp"], current_data["page_views"], label="Page Views")
        ax.plot(current_data["timestamp"], current_data["user_sessions"], label="User Sessions")
        ax.legend()
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("Count")
        ax.set_title("Live Page Views and User Sessions")
        chart_placeholder.pyplot(fig)  # Update the existing chart
        plt.close(fig)  # Close the figure to avoid memory issues

    # ---- Simulated Google Analytics ----
    ga_data = pd.DataFrame({
        "Page": ["Home", "About", "Contact"],
        "Page Views": np.random.randint(100, 500, size=3),
        "Unique Users": np.random.randint(50, 300, size=3),
    })
    placeholder_ga.dataframe(ga_data)

    # ---- Simulated LogRocket ----

    # Display LogRocket Logs in a nicely formatted table
    if np.random.rand() > 0.8:  # Randomly simulate user interactions
        log_rocket_logs.append({"Time": time.strftime('%H:%M:%S'), "Interaction": "Button Clicked"})

    # Convert logs to a DataFrame
    logrocket_df = pd.DataFrame(log_rocket_logs)

    if not logrocket_df.empty:
        # Show only the top 5 most recent logs
        recent_logs = logrocket_df.tail(5)
        
        # Display in a formatted table
        placeholder_logrocket.write(
            recent_logs.style.set_table_styles(
                [
                    {"selector": "thead th", "props": [("background-color", "black"), ("color", "white")]},
                    {"selector": "tbody td", "props": [("text-align", "left"), ("padding", "5px")]},
                ]
            ).set_caption("Most Recent 5 User Interaction Logs")
        )
    else:
        placeholder_logrocket.write("No interactions yet.")

    # ---- Simulated GrowthBook ----
    ab_test_results = pd.DataFrame({
        "Experiment": ["New Dashboard Design"],
        "Variant A Conversion Rate": [np.random.uniform(3.0, 5.0)],
        "Variant B Conversion Rate": [np.random.uniform(3.0, 5.0)],
        "Winner": ["Variant A" if np.random.rand() > 0.5 else "Variant B"]
    })
    placeholder_growthbook.dataframe(ab_test_results)

    # Pause for real-time effect
    time.sleep(1)
