# **Real-Time Analytics Dashboard (Simulation)**

This project implements a **Real-Time Analytics Dashboard** using [Streamlit](https://streamlit.io/). The dashboard simulates analytics data and displays key metrics in real-time, including:

- Real-Time Traffic Data (Page Views and User Sessions)
- Simulated Google Analytics Data
- Simulated LogRocket Interaction Logs
- Simulated GrowthBook A/B Testing Results

---

## **Features**

1. **Real-Time Traffic Data Visualization**:
   - A dynamically updating line chart displaying page views and user sessions.

2. **Google Analytics Simulation**:
   - Simulated page view and unique user data for key pages.

3. **LogRocket Interaction Logs**:
   - Dynamically logs and displays the **most recent 5 user interactions** in a formatted table.

4. **GrowthBook A/B Testing Simulation**:
   - Simulates A/B testing data and dynamically updates results in a clean table format.

---

## **Tech Stack**

- **Python**: Core programming language.
- **Streamlit**: Framework for building the real-time interactive dashboard.
- **Pandas**: Data handling and manipulation.
- **Matplotlib**: Visualization library for plotting real-time charts.

---

## **Setup Instructions**

### Prerequisites

- Install Python (>=3.7).
- Install required libraries listed in `requirements.txt`.

### Installation

1. Clone the repository:
   git clone https://github.com/premmody312/DataDash.git
   cd DataDash

2. Install dependencies:
   pip install -r requirements.txt

3. Run the application:
   streamlit run app.py

4. Open the provided URL (usually http://localhost:8501) in your browser.
