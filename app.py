import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)

st.title("🏠 House Price Prediction")
st.write("Predict house prices using Machine Learning")

# User inputs
area = st.number_input("Area", min_value=0, value=2000)
bedrooms = st.number_input("Bedrooms", min_value=1, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, value=2)
floors = st.number_input("Floors", min_value=1, value=2)
age = st.number_input("Age", min_value=0, value=10)
distance = st.number_input("Distance", min_value=0.0, value=10.0)

garage = st.number_input("Garage", min_value=0, value=1)
parking = st.number_input("Parking", min_value=0, value=1)
garden = st.number_input("Garden", min_value=0, max_value=1, value=0)
security = st.number_input("Security", min_value=0, max_value=1, value=1)

school_nearby = st.number_input(
    "School Nearby", min_value=0, max_value=1, value=1
)

hospital_nearby = st.number_input(
    "Hospital Nearby", min_value=0, max_value=1, value=1
)

shopping_mall_nearby = st.number_input(
    "Shopping Mall Nearby", min_value=0, max_value=1, value=1
)

public_transport = st.number_input(
    "Public Transport", min_value=0, max_value=1, value=1
)

crime_rate = st.number_input(
    "Crime Rate", min_value=0.0, value=5.0
)

population_density = st.number_input(
    "Population Density", min_value=0, value=5000
)

location = st.selectbox(
    "Location",
    ["low", "medium", "premium"]
)

income_level = st.selectbox(
    "Income Level",
    ["low", "mid", "high"]
)

if st.button("Predict House Price"):

    input_data = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "floors": floors,
        "age": age,
        "distance": distance,
        "garage": garage,
        "parking": parking,
        "garden": garden,
        "security": security,
        "school_nearby": school_nearby,
        "hospital_nearby": hospital_nearby,
        "shopping_mall_nearby": shopping_mall_nearby,
        "public_transport": public_transport,
        "crime_rate": crime_rate,
        "population_density": population_density,
        "location": location,
        "income_level": income_level
    }])

    prediction = model.predict(input_data)[0]

    st.success(
        f"🏠 Predicted House Price: {prediction:,.2f}"
    )
