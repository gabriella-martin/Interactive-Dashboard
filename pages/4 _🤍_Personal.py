
import important_metrics as im
import importlib
import streamlit as st
import streamlit_nested_layout
import pandas as pd
import plotly.express as px
from resources import visuals

from streamlit_extras.app_logo import add_logo
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_pills import pills
from instant_pipelines import welcome_pipeline


# styling

st.write("""<style>@import url('https://fonts.googleapis.com/css2?family=Kanit');html, body, [class*="css"]  {  
   font-family: 'Kanit';  
}</style>""", unsafe_allow_html=True)
color = '#6e6056'

style_metric_cards( background_color = color,border_left_color=color, border_size_px =0.3, border_color=color, border_radius_px=10)
add_logo("resources/logo_transparent_background.png", height=210)


#loading data and important metrics

@st.cache()
def get_data():
    df = pd.read_csv('data/database.csv')
    return df

df = get_data()

spotify = welcome_pipeline.SpotifyPipeline()
top_tracks = spotify.get_top_tracks()
airtable=welcome_pipeline.AirTablePipeline()
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
st.markdown(f"<a  href='#linkto_data' style='color: #FDF4DC;'>💡Click here for data details</a>", unsafe_allow_html=True)

st.write('')


# first row

if date_range == 'Yesterday':
    values = yesterdays_metrics
    deltas = yesterday_vs_day_before_yesterday_percent_change
if date_range == '3 Day Average':
    values = three_day_averages
    deltas = current_three_day_vs_past_three_day
if date_range == '7 Day Average':
    values = seven_day_averages
    deltas = current_seven_day_vs_past_seven_day

columns = st.columns(6)

columns[0].metric(label='Overall %', value=values[0], delta=str(deltas[0]) + '%')
columns[1].metric(label="Dogs %", value=values[1], delta=str(deltas[1]) + '%')
columns[2].metric(label="Cleaning %", value=values[2], delta=str(deltas[2]) + '%')
columns[3].metric(label="Self-Care %", value=values[3], delta=str(deltas[3]) + '%')
with columns[4]:
    value = values[4]
    emoji = get_mood_emoji(value)
    st.write(f'## Mood: {emoji}')
with columns[5]:
    st.write(f'## Sleep: {values[5]}hrs')


st.write('')
st.write('')

# second row

outer_cols = st.columns(2)

with outer_cols[0]:
     
        with st.expander('📖 **Currently Reading**', expanded=True):
          
            col1,col2,col3= st.columns(3)

            with col1:
                st.write('Read: ' + currently_reading[1][0] + '%')
                st.image(image=currently_reading[0][0])

            with col2 :
                st.write('Read: ' + currently_reading[1][1] + '%')
                st.image(image=currently_reading[0][1])
                
            with col3:
                st.markdown( 'Read: ' +   currently_reading[1][2] + '%')
                st.image(image=currently_reading[0][2])
                

with outer_cols[1]:

    with st.expander(' **📘 Just Read** ', expanded=True):
    
        col1,col2,col3 =st.columns(3)
        col1.write('Rating: ' + just_read[1] + '/5')
        col1.image(just_read[0])
        col2.write('Rating: ' + just_read[3] + '/5')
        col2.image(just_read[2])
        col3.write('Rating: '+ just_read[5] + '/5')
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
# behind the scenes
st.markdown(f"<div id='linkto_data'></div>", unsafe_allow_html=True)
data = st.write('')
 
with st.expander(label='Data Details: Behind the Scenes', expanded=True):
    st.write('')
    with st.expander(label='Data Pipeline'):

        st.write('**The full code for my personal pipeline can be viewed [here]( https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/Pipelines/Personal-Data-Pipeline.py) and also [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/Data-Pipeline.py)**')
        st.write("### • Retrieving ToDo's Done Data")

        cols = st.columns([0.2,6,0.2])
        cols[1].write("I organise my daily life with [ToDoist]( https://todoist.com/), who have a great [API]( https://developer.todoist.com/guides/) where each night my Python script retrieves the percentage of tasks in each section I have completed that day. I separate the task into sections by creating projects in ToDoist.  As the majority of my tasks are recurring, some manipulation with Python is necessary to retrieve what has been completed today. These daily percentages are then added to my CSV database file for visualisation with Pandas ")



        st.write('### • Retrieving Book Data')
        cols = st.columns([0.2,6,0.2])
        cols[1].write("I have been an avid user of [Goodreads]( https://www.goodreads.com/user/show/108711145-gabriella-martin) to track my reading progress but although they did have a solid API, they are discontinuing it and no longer issuing keys. However, I use [Airtable]( https://airtable.com/) to store much of my personal data and began to add my book tracking data. I then used their [API]( https://airtable.com/developers/web/api/introduction) to get my most recently read and currently reading books. Rather than being added daily to a CSV, this is instead called whenever the page is loaded in order to get an automatic update")

        st.write('### • Retrieving Listening Data')
        cols = st.columns([0.2,6,0.2])
        cols[1].write("As a Spotify user I love their [API]( https://developer.spotify.com/documentation/web-api/). There are many options for data to pull about your listening habits and I use a couple throughout the dashboard. Here I pull my recent top tracks so I can see what I have had on repeat recently. This is also not added to the CSV database and is again pulled automatically when the page is loaded")
        st.write("### • Retrieving Mood")
        cols = st.columns([0.2,6,0.2])
        cols[1].write("Again, for my mood tracker I use [Exist](https://exist.io), it really is a great all round personal tracker. I set a mood score on how I think my day has gone on a scale of 1-9. This is pulled once nightly via their [API]( https://developer.exist.io/)  and added to my CSV database for visualisation with Pandas")
        st.write('')
        st.write('')

    with st.expander(label='Visualisation'):
        visuals.personal_visual()
    
    with st.expander(label='Future Roadmap'):
        st.write('screen time')


