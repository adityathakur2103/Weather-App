import streamlit as st
import requests

api_key = '0254f81b872e3e546bc340f0b142d997'

st.title("Weather App")

location = st.text_input("Enter a city name: ")

if location:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"].capitalize()
        temperature = round(data["main"]["temp"] - 273.15, 2)
        humidity = data["main"]["humidity"]

        st.write(f"Weather in {location} : {weather_description}")
        st.write(f"Temperature : {temperature}°C")
        st.write(f"Humidity : {humidity}%")
    else:
        st.write("City not found. Please enter valid city name.")