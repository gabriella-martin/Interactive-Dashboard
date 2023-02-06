
import important_metrics as im
import importlib 
import pickle
import public_api_pipeline
import random
import streamlit as st
import streamlit_nested_layout

from datetime import datetime
from streamlit_extras.app_logo import add_logo
from streamlit_card import card
from streamlit_extras.let_it_rain import rain
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_player import st_player

st.set_page_config(
    page_title="Gabriella's Dashboard",
    page_icon="logo_transparent_background.png",
    layout="wide",
    initial_sidebar_state='auto')


st.write("""<style>@import url('https://fonts.googleapis.com/css2?family=Kanit');html, body, [class*="css"]  {  
   font-family: 'Kanit';  
}</style>""", unsafe_allow_html=True)

color = '#6e6056'

style_metric_cards( background_color = color,border_left_color=color, border_size_px =0.3, border_color=color, border_radius_px=10)
add_logo("logo_transparent_background.png", height=210)


metric_list = ['Overall', 'Health', 'Productivity', 'Personal']

overall_metrics = im.ImportantMetrics(metric_list=metric_list)

DataPipeline = importlib.import_module('Data-Pipeline')

a=DataPipeline.TodoistPipeline()
todays_tasks = a.get_todays_tasks()
a=DataPipeline.SpotifyPipeline()
currently_playing = a.get_currently_playing()
nasa_image = public_api_pipeline.nasa_image_of_the_day()

with st.sidebar:
    st.image(nasa_image[0],  caption='NASA Image of the Day: ' + nasa_image[1], width=450, use_column_width=True)


yesterdays_metrics = overall_metrics.get_time_period_metric(1)
yesterday_vs_day_before_yesterday_percent_change = overall_metrics.get_time_period_percent_change(1)
three_day_averages = overall_metrics.get_time_period_metric(3)
current_three_day_vs_past_three_day = overall_metrics.get_time_period_percent_change(3)
seven_day_averages = overall_metrics.get_time_period_metric(7)
current_seven_day_vs_past_seven_day = overall_metrics.get_time_period_percent_change(7)

with open('footie', 'rb') as fb:
    football_widget = pickle.load(fb)

weather  = public_api_pipeline.get_weather()
dlr_status = public_api_pipeline.tube_status_emoji()

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

st.write(f'# Good {greeting}, Gabriella')
st.write('')

sunrise_text = (str(weather[0]) + 'am')
sunset_text = (str(weather[1]) + 'pm')
temp_text = str(weather[2]) +  '\N{DEGREE SIGN}' + 'C'
condition = public_api_pipeline.get_condition_emoji()


today = str(datetime.today())
today = today[:10]
st.write(f"##### Today: :orange*{today}* | {temp_text} {condition} | ☀️{sunrise_text} |🌙{sunset_text} | 🚆 DLR: {dlr_status}")
st.write('')
st.write('')


outer_cols = st.columns([13, 4])

with outer_cols[0]:
    inner_cols = st.columns(2)
    with inner_cols[0]:
        
        card(
    title='HEALTH',
    text="",
    image="https://images.unsplash.com/photo-1528498033373-3c6c08e93d79?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=685&q=80",
    url="https://gabriella-martin-interactive-dashboard-welcome-9hpibj.streamlit.app/Health", 
)

        card(
    title='PERSONAL',
    text="",
    image="https://images.unsplash.com/photo-1556229167-7ed11195e641?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
    url="https://gabriella-martin-interactive-dashboard-welcome-9hpibj.streamlit.app/Personal", 
)
    with inner_cols[1]:

        card(
    title='PRODUCTIVITY',
    text="",
    image="https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1472&q=80",
    url="https://gabriella-martin-interactive-dashboard-welcome-9hpibj.streamlit.app/Productivity", 
)
        card(
    title='FINANCIAL',
    text="",
    image="https://images.unsplash.com/photo-1628873041000-857b83258b82?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
    url="https://gabriella-martin-interactive-dashboard-welcome-9hpibj.streamlit.app/Financial", 
)


with outer_cols[1]:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    with st.expander("☑️ **Today's Tasks**", expanded=False):

        for task in todays_tasks:
            st.write(task)

    with st.expander('👹 **Manchester United**', expanded=False):

        st.write(f'<center> {football_widget[3]} </center>' + '  \n' +  f'<center> {football_widget[4]}</center>', unsafe_allow_html=True)
        st.write('')
        inner_cols = st.columns([0.2,1,1,0.2])
        inner_cols[1].image(football_widget[1], width=60)
        inner_cols[2].image(football_widget[2], width=60)

    with st.expander('🎵 **Currently Playing**', expanded=False):
        st.write(f'<center> {currently_playing[0]}: </center>' + '  \n' + f'<center> {currently_playing[1]}</center>', unsafe_allow_html=True)
        inner_cols = st.columns([0.5,3, 0.5])
        with inner_cols[1]:
            st.image(image=currently_playing[2], use_column_width=True)






    
    


