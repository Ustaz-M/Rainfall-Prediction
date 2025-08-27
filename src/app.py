import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Rainfall Prediction", layout="centered")
st.title("🌧️ Rainfall Prediction")

# Load model
model = pickle.load(open(r"src\rainfall_prediction_model.pkl", "rb"))

#  MANUAL INPUT SECTION 
st.subheader("📥 Enter Feature Values")

 
pressure = st.number_input("Pressure")
maxtemp= st.number_input("Max Temp")
temperature = st.number_input("Temperature")
mintemp= st.number_input("Min Temp")
dewpoint= st.number_input("Dewpoint")
humidity = st.number_input("Humidity")
cloud= st.number_input("Cloud")
rainfall= st.number_input("Rainfall")
sunshine= st.number_input("Sunshine")
winddirection= st.number_input("Wind Direction")
wind_speed = st.number_input("Wind Speed")


#  PREDICTION 
if st.button("Predict Rainfall"):
    # Construct a DataFrame with the inputs
    input_df = pd.DataFrame([[temperature, humidity, pressure, wind_speed]],
                            columns=["Temperature", "Humidity", "Pressure", "Wind Speed"])

    # Predict
    prediction = model.predict(input_df)
    st.success(f"🌦️ Predicted Rainfall: {prediction[0]:.2f} mm")
