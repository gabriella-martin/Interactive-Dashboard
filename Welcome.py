import streamlit as st
from streamlit_extras.mention import mention
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
import requests
import datetime
from datetime import datetime
from datetime import date
from decouple import config
from public_api_pipeline import *
from streamlit_player import st_player
import random
add_logo("missmartin.jpeg", height=150)

st.write("# Personal Dashboard")

st.write('yas my name')

def get_greeting():
    today = str(datetime.now())
    today = today[10:13]
    today = int(today)
    if today < 12:
        greeting = 'Morning'
    if today >=12 and today <18:
        greeting = 'Afternoon'
    if today >=18:
        greeting ='Evening'
    return greeting
    

greeting = get_greeting()

#medium_link = mention(label='Medium Article', icon='✍🏽', url='https://google.com')

col1, col2 = st.columns([7,2])
today = str(date.today())
col1.write("##### Today: " + f":violet[*{today}*]")
col2.write('**Next United Match:**')




football_widget = football_api_process()

col1, col2, col3 = st.columns([6,0.85,0.85])
col1.write(f'#### Good {greeting}, Gabriella')  
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
    st.image(nasa_image, caption='NASA Image of the Day', width=147)



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
    

