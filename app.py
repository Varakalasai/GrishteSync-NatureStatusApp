# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import streamlit as st
import requests
import json

st.image('https://i.ibb.co/RGmb4FKk/1781072041102.png', width=200)

st.title('NatureStatusApp')

city = st.text_input('Enter city name')

if city:
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_OPENWEATHERMAP_API_KEY&units=metric'
        response = requests.get(url)
        data = response.json()
        st.write(f'Current weather in {city}:')
        col1, col2, col3 = st.columns(3)
        col1.metric('Temperature', f'{data['main']['temp']}°C')
        col2.metric('Humidity', f'{data['main']['humidity']}%')
        col3.metric('Weather', data['weather'][0]['main'])
    except Exception as e:
        st.error('City not found or invalid API key')

st.markdown('Made with GrishteSync | Suryasticsai | <a href="https://suryasticsai.github.io/GrishteSync">https://suryasticsai.github.io/GrishteSync</a>')