
import streamlit as st
from streamlit_extras.app_logo import add_logo
add_logo("logo_transparent_background.png", height=150)
from decouple import config
import requests
import base64

tab1, tab2, tab3 = st.tabs(["Welcome", "Overall", "Health"])


with tab1:
    st.write('include price')
    st.markdown("<h3 style='text-align: center;color: black;'>Creating My Welcome Page</h3>", unsafe_allow_html=True)

    st.write('On this page, the goal was to add all the core data I would need on a daily basis, first the weather. ')
    st.write('')
    st.write('1. **Weather API**' +    '  \n'  'I wanted to showcase the following weather metrics; current temperature, current condition, sunset and sunset. I used link(OpenWeather’s ) One Call REST API 3.0 to grab this. The current condition was a short phrase, but I wrote a function to convert this to the corresponding emoji. See the code for the API below:')
    


    body = '''def get_weather():
    key = config('WEATHER_API_KEY')
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat=51.46&lon=0.01&exclude=minutely,hourly,daily,alerts&appid={key}&units=metric'
    response = (requests.get(url)).json()
    json_response = response

    sunrise_time_epoch = json_response['current']['sunrise']
    sunset_time_epoch = json_response['current']['sunset']
    temperature = round(json_response['current']['temp'])
    condition = (json_response['current']['weather'][0]['description']).title()
    sunrise_time = datetime.fromtimestamp(sunrise_time_epoch).strftime('%H:%M')
    sunset_time = datetime.fromtimestamp(sunset_time_epoch).strftime('%I:%M')

    return(sunrise_time, sunset_time, temperature, condition)'''

    st.code(body, language="python")

    st.write('2. **Tube Status**')
    st.write("I leveraged TFL's impressive LINK(API) to get the status of the tube line I primarily use")



