
import importlib  
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
from streamlit_extras.stoggle import stoggle





DataPipeline = importlib.import_module('Data-Pipeline')
a=DataPipeline.ExistPipeline()

with open('footie', 'rb') as fb:
    football_widget = pickle.load(fb)

st.write("# Personal Dashboard")

today = str(datetime.now())
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

from public_api_pipeline import *
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
today = str(datetime.today())
today = today[:10]
col1.write(f"##### Today: :violet[*{today}*] | {temp_text} {condition} | ☀️{sunrise_text} |🌙{sunset_text}")

col2.write(f'+ **{football_widget[3]}**')

b = DataPipeline.GoogleCalendarPipeline()
todays_events = b.get_todays_events()

recent_contributions = a.get_github_contributions()

col1, col2, col3, col4, col5 = st.columns([6,2.2,2.2,1.5,1.5])
col1.write(f'### Good {greeting}, Gabriella')  
col1.markdown("**Today's Schedule**")
col2.metric(label = ('Git Today:'), value = recent_contributions[1])
col3.metric(label='Yesterday:', value=recent_contributions[0])


col4.image(football_widget[1])
col5.image(football_widget[2])

col1, col2 = st.columns([7,2])







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

def get_calendar_emoji():
    for event in todays_events:
        if 'Dog' in event[0]:
            event[0] = '🐾 ' + event[0]
        elif 'Gym' in event[0]:
            event[0] = '💣 ' + event[0]
        elif 'Work' in event[0]:
            event[0] = '👩🏽‍💻 ' + event[0]
        elif 'Clean' in event[0]:
            event[0] = '🧽 ' + event[0]
    return todays_events


todays_events = get_calendar_emoji()

number_of_events_today = len(todays_events)
from annotated_text import annotated_text, annotation

def get_each_cal_event():
    event_rows = []
    for i in range(0,number_of_events_today):
        time_of_day = (todays_events)[i][1] + '-' + (todays_events)[i][2]
        name_of_event = todays_events[i][0]
        event_row = annotated_text("", (name_of_event, time_of_day, '#f7dfeb', "5px black"))
        event_rows.append(event_row)
    return event_rows




mood_data = a.get_mood_data()
mood_data = list(mood_data)
sleep_data = a.get_sleep_data()

def get_recap_and_overview(mood_data):
    mood_data[1] =mood_data[1].split(',')
    mood_data[1][0] = mood_data[1][0].split('/')
    mood_data[1][1] = mood_data[1][1].split('/')
    return mood_data[1]


mood_data[1] = get_recap_and_overview(mood_data)



def get_mood_emoji(mood_data):
    if mood_data[0] == 9:
        mood_data[0] = '🤩'
    elif mood_data[0] <9 and mood_data[0] >= 7:
        mood_data[0] = '😆'
    elif mood_data[0] <7 and mood_data[0] >= 5:
        mood_data[0] = '🙂'   
    elif mood_data[0] <5 and mood_data[0] >=3:
        mood_data[0] = '😐'
    else:
        mood_data[0] ='😶'
    return mood_data[0]

mood_data[0] = get_mood_emoji(mood_data)

col1, col2, col3 = st.columns([7,7,4])
with col1:

    event_rows = get_each_cal_event()
    
    

with col2:
    st.metric(label = 'Sleep', value = sleep_data[0])
    st.metric(label = 'Awake', value = sleep_data[1])
    st.write(f'##### Mood Yesterday: {mood_data[0]}')
    #st.write(mood_data[1])
with col3:
    
    nasa_image_of_the_day()
    
col1, col2 = st.columns([7,2])

b = DataPipeline.AirTablePipeline()
currently_reading_covers = b.get_currently_reading_books()
number_of_books_reading = len(currently_reading_covers)






with col1:
    st.write('')
    st.write('')
    st.write('##### Goals for Today:')

    for i in range(0,3):
        st.text(f'{mood_data[1][1][i]}')
    
    st.write('')
    st.write('')
    st.write('##### Yesterday Recap:')

    for i in range(0,3):
        st.text(f'{mood_data[1][0][i]}')


    
    

with col2:
    selection = st.selectbox(label ='What is the soundtrack for today?', options=['Summer Temptations', 'Urban Volume', 'Sugar Baby', '90s Club Classics'])
    

    dj_mix_dict = {'Summer Temptations':'https://soundcloud.com/missmartindj/summer-temptations-minimix-1','Urban Volume':'https://soundcloud.com/missmartindj/urban-volume-i',
    'Sugar Baby':'https://soundcloud.com/missmartindj/sugar-baby-volume-i','90s Club Classics':'https://soundcloud.com/missmartindj/9ts-baby-club-clasics'}

    for mix in dj_mix_dict.keys():
        if selection == mix:
            url = dj_mix_dict[mix]
    st_player(url=url, height=300, playing=False)


st.write('tube status, ')