import streamlit as st
from streamlit_extras.mention import mention
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
import requests


from decouple import config
from public_api_pipeline import *
from streamlit_player import st_player
import random
import pickle
add_logo("logo_transparent_background.png", height=150)


from Data_Pipeline import *

with open('footie', 'rb') as fb:
    football_widget = pickle.load(fb)

st.write("# Personal Dashboard")

today = str(datetime.datetime.now())
hour = today[10:13]

def get_greeting(hour):
    
    hour = int(hour)
    if hour < 12:
        greeting = 'Morning'
    if hour >=12 and hour <18:
        greeting = 'Afternoon'
    if hour >=18:
        greeting ='Evening'
    return greeting
    

greeting = get_greeting(hour)

#medium_link = mention(label='Medium Article', icon='✍🏽', url='https://google.com')


weather  = get_weather()

sunrise_text = (str(weather[0]) + 'am')
sunset_text = (str(weather[1]) + 'pm')
temp_text = str(weather[2]) +  '\N{DEGREE SIGN}' + 'C'
description = weather[3]

def get_condition_emoji(description):
    if 'Thunderstorm' in description:
        condition_emoji = '⚡'
    elif 'Drizzle' in description:
        condition_emoji ='💧'
    elif 'Rain' in description:
        condition_emoji ='🌧️'
    elif 'Snow' in description:
        condition_emoji ='❄️'
    elif 'Clear Sky' in description:
        condition_emoji = '🌤'
    elif 'Clouds' in description:
        condition_emoji ='️🌥'
    else:
        condition_emoji = '🌫️'
        
    return condition_emoji

condition = get_condition_emoji(description)

col1, col2 = st.columns([7,2])
today = str(datetime.datetime.today())
today = today[:10]
col1.write(f"##### Today: :violet[*{today}*] | {temp_text} {condition} | ☀️{sunrise_text} |🌙{sunset_text}")
col2.write('**Next United Match:**')

a = GoogleCalendarPipeline()
todays_events = a.get_todays_events()
col1, col2, col3 = st.columns([6,0.85,0.85])
col1.write(f'#### Good {greeting}, Gabriella')  
col1.write(f'Welcome, here are your events for today:')
for event in todays_events:
    col1.write(f'{event}')

##




col2.image(football_widget[1])
col3.image(football_widget[2])
col1, col2 = st.columns([7,2])
col2.write(f'**{football_widget[3]}**')



def get_quote():
    url = 'https://stoicquotesapi.com/v1/api/quotes/random'
    response = requests.get(url)
    quote = (response.json()).get('body')
    

get_quote()

def nasa_image_of_the_day():
    url = 'https://api.nasa.gov/planetary/apod?api_key=PZcnX4xvaDZt6n394qdhjTT9p9Jvwex3oTqMofpt'
    response = requests.get(url)
    nasa_image = (response.json())['hdurl']
    st.image(nasa_image, caption='NASA Image of the Day', width=150)



col1, col2 = st.columns([7,2])
with col1:

    pass

with col2:
    nasa_image_of_the_day()
    selection = st.selectbox(label ='What is the soundtrack for today?', options=['Summer Temptations', 'Urban Volume', 'Sugar Baby', '90s Club Classics'])
    

    dj_mix_dict = {'Summer Temptations':'https://soundcloud.com/missmartindj/summer-temptations-minimix-1','Urban Volume':'https://soundcloud.com/missmartindj/urban-volume-i',
    'Sugar Baby':'https://soundcloud.com/missmartindj/sugar-baby-volume-i','90s Club Classics':'https://soundcloud.com/missmartindj/9ts-baby-club-clasics'}

    for mix in dj_mix_dict.keys():
        if selection == mix:
            url = dj_mix_dict[mix]
    st_player(url=url, height=300, playing=False)
    