
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


#loading data and important metrics

@st.cache()
def get_data():
    df = pd.read_csv('Database.csv')
    return df

df = get_data()

spotify = DataPipeline.SpotifyPipeline()
airtable=DataPipeline.AirTablePipeline()
currently_reading = airtable.get_currently_reading_books()
productivity_metrics = im.ImportantMetrics(metric_list = ['Personal', 'Dogs', 'Cleaning', 'Self-Care', 'Mood'])
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


st.markdown("<h1 style='text-align: center;color: #FDF4DC;'>Personal Hub</h1>", unsafe_allow_html=True)
st.write('')


# first row


date_range = st.select_slider(label = 'What date range would you like to see?', options = ['Yesterday', '3 Days', '7 Days'], label_visibility = 'collapsed')

outer_cols = st.columns([7,0.3,1])

with outer_cols[0]:

    if date_range == '3 Days':
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Personal", value=three_day_averages[0], delta=str(current_three_day_vs_past_three_day[0]) + '%')
        col2.metric(label="Dogs", value=three_day_averages[1], delta=str(current_three_day_vs_past_three_day[1]) + '%')
        col3.metric(label="Cleaning", value=three_day_averages[2], delta=str(current_three_day_vs_past_three_day[2]) + '%')
        col4.metric(label="Self-Care", value=three_day_averages[3], delta=str(current_three_day_vs_past_three_day[3]) + '%')
    if date_range == '7 Days':
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Personal", value=seven_day_averages[0], delta=str(current_seven_day_vs_past_seven_day[0]) + '%')
        col2.metric(label="Dogs", value=seven_day_averages[1], delta=str(current_seven_day_vs_past_seven_day[1]) + '%')
        col3.metric(label="Cleaning", value=seven_day_averages[2], delta=str(current_seven_day_vs_past_seven_day[2]) + '%')
        col4.metric(label="Self-Care", value=seven_day_averages[3], delta=str(current_seven_day_vs_past_seven_day[3]) + '%')
    if date_range == 'Yesterday':
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Personal", value=yesterdays_metrics[0], delta=str(yesterday_vs_day_before_yesterday_percent_change[0]) + '%')
        col2.metric(label="Dogs", value=yesterdays_metrics[1], delta=str(yesterday_vs_day_before_yesterday_percent_change[1]) + '%')
        col3.metric(label="Cleaning", value=yesterdays_metrics[2], delta=str(yesterday_vs_day_before_yesterday_percent_change[2]) + '%')
        col4.metric(label="Self-Care", value=yesterdays_metrics[3], delta=str(yesterday_vs_day_before_yesterday_percent_change[3]) + '%')

with outer_cols[2]:
   
    if date_range == 'Yesterday':
        value = yesterdays_metrics[4]
        emoji = get_mood_emoji(value)
        st.write('## Mood:' +  f'{emoji}')

    if date_range == '3 Days':
        value = three_day_averages[4]
        emoji = get_mood_emoji(value)
        st.write('## Mood:' +  f'{emoji}')

    if date_range == '7 Days':
        value = seven_day_averages[4]
        emoji = get_mood_emoji(value)
        st.write('## Mood:' +  f'{emoji}')

st.write('')
st.write('')

# second row

outer_cols = st.columns([10,14])

with outer_cols[0]:
     
        with st.expander('📖 **Currently Reading**', expanded=True):
          
            col1,col2,col3= st.columns(3)

            with col1:
            
                st.image(image=currently_reading[0][0], use_column_width='always')
                st.write(currently_reading[1][0] + '%')


            with col2 :
            
                st.image(image=currently_reading[0][1], use_column_width='always')
                st.write(currently_reading[1][1] + '%')
            with col3:
            
                st.image(image=currently_reading[0][2], use_column_width='always')
                st.write(currently_reading[1][2] + '%')

with outer_cols[1]:

    with st.expander(' **🎵 Top Songs** ', expanded=True):
        st.write('')
        top_songs = spotify.get_top_tracks()

        col1,col2,col3 =st.columns(3)
        
        col1.image(top_songs[0][2], width=100)
        col1.write(top_songs[0][0])

        col2.image(top_songs[1][2], width=100)
        col2.write(top_songs[1][0])
        
        col3.image(top_songs[2][2], width=100)
        col3.write(top_songs[2][0])
        
       
with st.expander(label = '**Full Spotify Stats**', expanded=False):
    st.markdown(body = '<a href="https://www.data-card-for-spotify.com/card?user_id=djgabriellamartin"><img src="https://www.data-card-for-spotify.com/api/card?user_id=djgabriellamartin&hide_top_artists=1" alt="Data Card for Spotify"></a>', unsafe_allow_html=True)


# line graph of long term data


selected = pills('What to visualise', ['Personal', 'Dogs', 'Cleaning', 'Self-Care', 'Mood'], ['❤️‍🩹', '🐾', '🧽','💌', '😏'], label_visibility='collapsed')

if selected == 'Personal' or selected == 'Dogs' or selected == 'Cleaning' or selected == 'Self-Care':
    fig = px.line(df, x='Days', y =[selected, 'Goal Score'], color_discrete_sequence=["#6e6056", "#e5ddd3"])
    fig.update(layout_yaxis_range = [50,130])
    st.plotly_chart(fig, use_container_width=True)

else:
    fig = px.line(df, x='Days', y =selected, color_discrete_sequence= ["#6e6056"])
    st.plotly_chart(fig, use_container_width=True)  



