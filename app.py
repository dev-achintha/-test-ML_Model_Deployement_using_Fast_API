import streamlit as st
import requests
import json

st.title("Diabetes Prediction")

pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose Level", min_value=0, step=1)
blood_pressure = st.number_input("Blood Pressure", min_value=0, step=1)
skin_thickness = st.number_input("Skin Thickness", min_value=0, step=1)
insulin = st.number_input("Insulin Level", min_value=0, step=1)
bmi = st.number_input("BMI", min_value=0.0, step=0.1)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, step=0.1)
age = st.number_input("Age", min_value=0, step=1)

if st.button("Predict"):
    url = "https://your-vercel-deployment-url.vercel.app/api/diabetes_prediction"
    params = {
        "pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": diabetes_pedigree,
        "Age": age
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        result = response.json()
        st.write(result)
    except requests.exceptions.JSONDecodeError:
        st.error("Error decoding the response. Please try again later.")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")