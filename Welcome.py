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
add_logo("missmartin.jpeg", height=250)

st.write("# Gabriella's Dashboard")



def get_greeting():
    today = str(datetime.now())
    today = today[10:13]
    today = int(today)
    if today < 12:
        greeting = 'Morning'
    if today >12 and today <18:
        greeting = 'Afternoon'
    else:
        greeting ='Evening'
    return greeting
    

greeting = get_greeting()

#medium_link = mention(label='Medium Article', icon='✍🏽', url='https://google.com')

col1, col2 = st.columns([7,2])
today = str(date.today())
col1.write("##### Today: " + f":violet[*{today}*]")
col2.write('**Next United Match:**')

football_widget = football_api_process()
def create_section(football_widget):

    col1, col2, col3 = st.columns([6,1,1])
    col1.write(f'#### Good {greeting}')  
    col2.image(football_widget[1])
    col3.image(football_widget[2])
    col1, col2 = st.columns([7,2])
    col2.write(f'**{football_widget[3]}**')

create_section(football_widget)

