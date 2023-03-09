
import important_metrics as im
import pickle
import streamlit as st
import streamlit_nested_layout
from resources import visuals
from datetime import datetime
from instant_pipelines import public_api_pipeline, welcome_pipeline
from streamlit_extras.app_logo import add_logo
from streamlit_extras.metric_cards import style_metric_cards

# styling

st.set_page_config(
    page_title="Gabriella's Dashboard",
    page_icon="resources/logo_transparent_background.png",
    layout="wide",
    initial_sidebar_state='auto')


st.write("""<style>@import url('https://fonts.googleapis.com/css2?family=Kanit');html, body, [class*="css"]  {  
   font-family: 'Kanit';  
}</style>""", unsafe_allow_html=True)

color = '#6e6056'

style_metric_cards( background_color = color,border_left_color=color, border_size_px =0.3, border_color=color, border_radius_px=10)
add_logo("resources/logo_transparent_background.png", height=210)

# loading important functions

metric_list = ['Overall', 'Health', 'Productivity', 'Personal']

overall_metrics = im.ImportantMetrics(metric_list=metric_list)
a=welcome_pipeline.TodoistPipeline()
todays_tasks = a.get_todays_tasks()
a=welcome_pipeline.SpotifyPipeline()
currently_playing = a.get_currently_playing()
nasa_image = public_api_pipeline.nasa_image_of_the_day()
weather  = public_api_pipeline.get_weather()
dlr_status = public_api_pipeline.tube_status_emoji()

with open('footie', 'rb') as fb:
    football_widget = pickle.load(fb)

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

# start of visual

st.write(f'# Good {greeting}, Gabriella')
st.write('')

sunrise_text = (str(weather[0]) + 'am')
sunset_text = (str(weather[1]) + 'pm')
temp_text = str(weather[2]) +  '\N{DEGREE SIGN}' + 'C'
condition = public_api_pipeline.get_condition_emoji()


today = str(datetime.today())
today = today[:10]
st.write(f"##### Today: :orange*{today}* | {temp_text} {condition} | ☀️{sunrise_text} |🌙{sunset_text} | 🚆 DLR: {dlr_status}")
st.markdown(f"<a  href='#linkto_data' style='color: #FDF4DC;'>💡Click here for data details</a>", unsafe_allow_html=True)



outer_cols = st.columns([13, 4])

with outer_cols[0]:
    st.image(nasa_image[0],  caption='NASA Image of the Day: ' + nasa_image[1], use_column_width=True)  

with outer_cols[1]:
    st.write('')

    with st.expander("☑️ **Today's Tasks**", expanded=True):

        for task in todays_tasks:
            st.write(task)

    with st.expander('👹 **Manchester United**', expanded=True):

        st.write(f'<center> {football_widget[3]} </center>' + '  \n' +  f'<center> {football_widget[4]}</center>', unsafe_allow_html=True)
        st.write('')
        inner_cols = st.columns([0.2,1,1,0.2])
        inner_cols[1].image(football_widget[1], width=60)
        inner_cols[2].image(football_widget[2], width=60)

    with st.expander('📻 **Currently Playing**', expanded=True):
        st.write(f'<center> {currently_playing[0]}: </center>' + '  \n' + f'<center> {currently_playing[1]}</center>', unsafe_allow_html=True)
        inner_cols = st.columns([0.5,3, 0.5])
        with inner_cols[1]:
            st.image(image=currently_playing[2], use_column_width=True)

st.markdown(f"<div id='linkto_data'></div>", unsafe_allow_html=True)
data = st.write('')

with st.expander(label='Behind the Scenes', expanded=True):
    st.write('')
    with st.expander(label='Data Pipeline'):

        st.write('**The full code for my welcome page pipeline can be viewed [here]( https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/Welcome.py)**')
        st.write("### • Retrieving Weather")

        cols = st.columns([0.2,6,0.2])
        cols[1].write("There are many options for a free weather API but I use [WeatherAPI.com]( https://www.weatherapi.com/). I retrieve the current temperature, current condition (which I format into an emoji), sunrise and sunset. This is called when the page loads to give up to date information")



        st.write('### • Retrieving Tube Status')
        cols = st.columns([0.2,6,0.2])
        cols[1].write("Transport for London have a wide variety of API endpoints, for my purposes as I tend to just use the DLR on a daily basis, I use their [API]( https://api.tfl.gov.uk/) to retrieve the current tube status. This is extracted whenever the page is loaded and formatted with a corresponding emoji")

        st.write('### • Retrieving Manchester United Data')
        cols = st.columns([0.2,6,0.2])
        cols[1].write("I hate to miss any of my team Manchester United’s games, so I use a football [API]( https://rapidapi.com/api-sports/api/api-football) to retrieve the important information about the next game; date, time, home or away, opponent and league. Again this is pulled once the page is loaded")
        st.write("### • Retrieving Spotify Data")
        cols = st.columns([0.2,6,0.2])
        cols[1].write("Spotify’s easy to use [API]( https://developer.spotify.com/documentation/web-api/) nicely integrates with the welcome page by delivering what I am currently listening to, if I am not listening to anything right now, instead it pulls my most recently listened to track")
        st.write("### • Retrieving Work ToDo List")
        cols = st.columns([0.2,6,0.2])
        cols[1].write("For my work tasks, I use ToDoist to pull my work-related tasks for the day, rather than process percentage of tasks complete as in the personal section, instead it retrieves the content of each task, giving me a clear overview of what work related tasks I have to do. Their [API]( https://developer.todoist.com/guides/#developing-with-todoist) is called each time the page loads to get a updated list of tasks")
        st.write('')
        st.write('')

    with st.expander(label='Visualisation'):
        visuals.welcome_visual()
    




    
    


