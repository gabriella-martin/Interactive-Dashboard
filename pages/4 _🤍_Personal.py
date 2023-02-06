
import important_metrics as im
import importlib
import streamlit as st
import streamlit_nested_layout
import pandas as pd
import plotly.express as px

from streamlit_extras.app_logo import add_logo
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_pills import pills
DataPipeline = importlib.import_module('Data-Pipeline')


# styling

st.write("""<style>@import url('https://fonts.googleapis.com/css2?family=Kanit');html, body, [class*="css"]  {  
   font-family: 'Kanit';  
}</style>""", unsafe_allow_html=True)
color = '#6e6056'

style_metric_cards( background_color = color,border_left_color=color, border_size_px =0.3, border_color=color, border_radius_px=10)
add_logo("logo_transparent_background.png", height=210)


#loading data and important metricsget_just_read_books

@st.cache()
def get_data():
    df = pd.read_csv('Database.csv')
    return df

df = get_data()

spotify = DataPipeline.SpotifyPipeline()
top_tracks = spotify.get_top_tracks()
airtable=DataPipeline.AirTablePipeline()
currently_reading = airtable.get_currently_reading_books()
just_read = airtable.get_just_read_books()
productivity_metrics = im.ImportantMetrics(metric_list = ['Personal', 'Dogs', 'Cleaning', 'Self-Care', 'Mood', 'Sleep'])
yesterdays_metrics = productivity_metrics.get_time_period_metric(1)
yesterday_vs_day_before_yesterday_percent_change = productivity_metrics.get_time_period_percent_change(1)
three_day_averages = productivity_metrics.get_time_period_metric(3)
current_three_day_vs_past_three_day = productivity_metrics.get_time_period_percent_change(3)
seven_day_averages = productivity_metrics.get_time_period_metric(7)
current_seven_day_vs_past_seven_day = productivity_metrics.get_time_period_percent_change(7)


# functions needed


emoji_list = ['🤩', '😆', '😃', '😀', '☺️', '🙂' ,'😐','😶', '😶' ]

def get_mood_emoji(value):
    index = 9 - value
    emoji = emoji_list[index]
    return emoji

# start of visual

with st.sidebar:
    st.markdown("<h4 style='text-align: center;color: #FDF4DC;'>Date Range Slider</t>", unsafe_allow_html=True)
    date_range = st.select_slider(label = 'DATE RANGE SLIDER', options = ['Yesterday', '3 Day Average', '7 Day Average'], label_visibility = 'collapsed')



st.markdown("<h1 style='text-align: center;color: #FDF4DC;'>Personal Hub</h1>", unsafe_allow_html=True)
st.write('')


# first row


columns = st.columns(6)

if date_range == '3 Day Average':
       
    columns[0].metric(label='Overall', value=three_day_averages[0], delta=str(three_day_averages[0]) + '%')
    columns[1].metric(label="Dogs", value=three_day_averages[1], delta=str(current_three_day_vs_past_three_day[1]) + '%')
    columns[2].metric(label="Cleaning", value=three_day_averages[2], delta=str(current_three_day_vs_past_three_day[2]) + '%')
    columns[3].metric(label="Self-Care", value=three_day_averages[3], delta=str(current_three_day_vs_past_three_day[3]) + '%')
    with columns[4]:
        value = yesterdays_metrics[4]
        emoji = get_mood_emoji(value)
        st.write(f'## Mood: {emoji}')
    with columns[5]:
        st.write(f'## Sleep: {three_day_averages[5]}hrs')
if date_range == '7 Day Average':

    columns[0].metric(label="Overall", value=seven_day_averages[0], delta=str(current_seven_day_vs_past_seven_day[0]) + '%')
    columns[1].metric(label="Dogs", value=seven_day_averages[1], delta=str(current_seven_day_vs_past_seven_day[1]) + '%')
    columns[2].metric(label="Cleaning", value=seven_day_averages[2], delta=str(current_seven_day_vs_past_seven_day[2]) + '%')
    columns[3].metric(label="Self-Care", value=seven_day_averages[3], delta=str(current_seven_day_vs_past_seven_day[3]) + '%')
    with columns[4]:
        value = three_day_averages[4]
        emoji = get_mood_emoji(value)
        st.write(f'## Mood: {emoji}')
    with columns[5]:
        st.write(f'## Sleep: {seven_day_averages[5]}hrs')
if date_range == 'Yesterday':
    columns[0].metric(label="Overall", value=seven_day_averages[0], delta=str(current_seven_day_vs_past_seven_day[0]) + '%')
    columns[1].metric(label="Dogs", value=yesterdays_metrics[1], delta=str(yesterday_vs_day_before_yesterday_percent_change[1]) + '%')
    columns[2].metric(label="Cleaning", value=yesterdays_metrics[2], delta=str(yesterday_vs_day_before_yesterday_percent_change[2]) + '%')
    columns[3].metric(label="Self-Care", value=yesterdays_metrics[3], delta=str(yesterday_vs_day_before_yesterday_percent_change[3]) + '%')
    with columns[4]:
        value = seven_day_averages[4]
        emoji = get_mood_emoji(value)
        st.write(f'## Mood: {emoji}')
    with columns[5]:
        st.write(f'## Sleep: {yesterdays_metrics[5]}hrs')

       

st.write('')
st.write('')

# second row

outer_cols = st.columns(2)

with outer_cols[0]:
     
        with st.expander('📖 **Currently Reading**', expanded=True):
          
            col1,col2,col3= st.columns(3)

            with col1:
                st.write(currently_reading[1][0] + '%')
                st.image(image=currently_reading[0][0], use_column_width='always')
                


            with col2 :
                st.write(currently_reading[1][1] + '%')
                st.image(image=currently_reading[0][1], use_column_width='always')
                
            with col3:
                st.write(currently_reading[1][2] + '%')
                st.image(image=currently_reading[0][2], use_column_width='always')
                

with outer_cols[1]:

    with st.expander(' **📘 Just Read** ', expanded=True):
    
        col1,col2,col3 =st.columns(3)
        col1.write(just_read[1] + '/5')
        col1.image(just_read[0])
        col2.write(just_read[3] + '/5')
        col2.image(just_read[2])
        col3.write(just_read[5] + '/5')
        col3.image(just_read[4])
        

with st.expander('🎹 Top Tracks', expanded=True):
    inner_cols = st.columns(6)
    for i in range(0,6):
        inner_cols[i].image(top_tracks[i][2], caption = top_tracks[i][0] )
    
       

# line graph of long term data

st.write('')
selected = pills('What to visualise', ['Personal', 'Dogs', 'Cleaning', 'Self-Care', 'Mood'], ['❤️‍🩹', '🐾', '🧽','💌', '😏'], label_visibility='collapsed')

if selected == 'Personal' or selected == 'Dogs' or selected == 'Cleaning' or selected == 'Self-Care':
    fig = px.line(df, x='Days', y =[selected, 'Goal Score'], color_discrete_sequence=["#6e6056", "#e5ddd3"])
    fig.update(layout_yaxis_range = [50,130])
    st.plotly_chart(fig, use_container_width=True)

else:
    fig = px.line(df, x='Days', y =selected, color_discrete_sequence= ["#6e6056"])
    st.plotly_chart(fig, use_container_width=True)  


