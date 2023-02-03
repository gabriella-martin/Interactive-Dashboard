
import important_metrics as im
import importlib 
import pickle
import public_api_pipeline
import random
import streamlit as st
import streamlit_nested_layout

st.set_page_config(
    page_title="Gabriella's Dashboard",
    page_icon="",
    layout="wide")
    
from datetime import datetime
from streamlit_extras.app_logo import add_logo
from streamlit_extras.let_it_rain import rain
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_player import st_player

color = '#6e6056'

style_metric_cards( background_color = color,border_left_color=color, border_size_px =0.3, border_color=color, border_radius_px=10)
add_logo("logo_transparent_background.png", height=160)


metric_list = ['Overall', 'Health', 'Productivity', 'Personal']

overall_metrics = im.ImportantMetrics(metric_list=metric_list)

DataPipeline = importlib.import_module('Data-Pipeline')

a=DataPipeline.TodoistPipeline()
todays_tasks = a.get_todays_tasks()
a=DataPipeline.SpotifyPipeline()
currently_playing = a.get_currently_playing()
nasa_image = public_api_pipeline.nasa_image_of_the_day()

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

col1, col2 = st.columns([7,2])
today = str(datetime.today())
today = today[:10]
col1.write(f"##### Today: :orange*{today}*] | {temp_text} {condition} | ☀️{sunrise_text} |🌙{sunset_text} | 🚆 DLR: {dlr_status}")
col1.write('')
col1.write('')


outer_cols = st.columns([13, 4])

with outer_cols[0]:

    col1,col2 = st.columns([7,3])
    col1.image(nasa_image, caption='NASA Image of the Day', width=450, use_column_width=True)
    with col2:
        with st.expander("☑️ **Today's Tasks**", expanded=True):

            for task in todays_tasks:
                st.write(task)

    date_range = st.select_slider(label = 'What date range would you like to see?', options = ['Yesterday', '3 Days', '7 Days'], label_visibility = 'collapsed')
    
    if date_range == '3 Days':

        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Overall", value=three_day_averages[0], delta=str(current_three_day_vs_past_three_day[0]) + '%')
        col2.metric(label="Health", value=three_day_averages[1], delta=str(current_three_day_vs_past_three_day[1]) + '%')
        col3.metric(label="Productivity", value=three_day_averages[2], delta=str(current_three_day_vs_past_three_day[2]) + '%')
        col4.metric(label="Personal", value=three_day_averages[3], delta=str(current_three_day_vs_past_three_day[3]) + '%')
    
    if date_range == '7 Days':

        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Overall", value=seven_day_averages[0], delta=str(current_seven_day_vs_past_seven_day[0]) + '%')
        col2.metric(label="Health", value=seven_day_averages[1], delta=str(current_seven_day_vs_past_seven_day[1]) + '%')
        col3.metric(label="Productivity", value=seven_day_averages[2], delta=str(current_seven_day_vs_past_seven_day[2]) + '%')
        col4.metric(label="Personal", value=seven_day_averages[3], delta=str(current_seven_day_vs_past_seven_day[3]) + '%')
    
    if date_range == 'Yesterday':

        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Overall", value=yesterdays_metrics[0], delta=str(yesterday_vs_day_before_yesterday_percent_change[0]) + '%')
        col2.metric(label="Health", value=yesterdays_metrics[1], delta=str(yesterday_vs_day_before_yesterday_percent_change[1]) + '%')
        col3.metric(label="Productivity", value=yesterdays_metrics[2], delta=str(yesterday_vs_day_before_yesterday_percent_change[2]) + '%')
        col4.metric(label="Personal", value=yesterdays_metrics[3], delta=str(yesterday_vs_day_before_yesterday_percent_change[3]) + '%')
        
        if yesterdays_metrics[0] >= 100:
            
            st.success('Congratulations, yesterday you hit your goal score!', icon='🎯')
            
        if yesterdays_metrics[0] <100 and yesterdays_metrics[0] >95:
            
            st.warning('So close! You nearly hit your target, try better today!', icon="⚠️")
            
        if yesterdays_metrics[0] <=95:
            
            st.error('Yesterday you were off track, try extra hard today!', icon='🚨')

with outer_cols[1]:

    with st.expander('👹 **Manchester United**', expanded=True):

        st.write(f'<center> {football_widget[3]} </center>' + '  \n' +  f'<center> {football_widget[4]}</center>', unsafe_allow_html=True)
        st.write('')
        col1,col2 = st.columns(2)
        col1.image(football_widget[1], width=60)
        col2.image(football_widget[2], width=60)

    with st.expander('🎵 **Currently Playing**', expanded=True):

        col1,col2 = st.columns(2)
        with col1:
            st.write('')
            st.write(f'<center> {currently_playing[0]}: </center>' + '  \n' + f'<center> {currently_playing[1]}</center>', unsafe_allow_html=True)
        with col2:
            st.image(image=currently_playing[2], use_column_width=True)

        st.write('☁️ **SoundCloud**')
        options = ['Summer Temptations', 'Urban Volume', 'Sugar Baby', '90s Club Classics']
        random.shuffle(options)
       
        selection = st.selectbox(label ='What is the soundtrack for today?', options=options, label_visibility='collapsed')

        dj_mix_dict = {'Summer Temptations':'https://soundcloud.com/missmartindj/summer-temptations-minimix-1','Urban Volume':'https://soundcloud.com/missmartindj/urban-volume-i',
        'Sugar Baby':'https://soundcloud.com/missmartindj/sugar-baby-volume-i','90s Club Classics':'https://soundcloud.com/missmartindj/9ts-baby-club-clasics'}

        for mix in dj_mix_dict.keys():
            if selection == mix:
                url = dj_mix_dict[mix]

        st_player(url=url, height=200, playing=False)





    
    


