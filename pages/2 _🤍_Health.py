
import important_metrics as im
import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit_nested_layout
import Visuals

from streamlit_extras.app_logo import add_logo
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_pills import pills

#styling

st.write("""<style>@import url('https://fonts.googleapis.com/css2?family=Kanit');html, body, [class*="css"]  {  
   font-family: 'Kanit';  
}</style>""", unsafe_allow_html=True)

color = '#6e6056'

style_metric_cards( background_color = color,border_left_color=color, border_size_px =0.3, border_color=color, border_radius_px=10)
add_logo("images/logo_transparent_background.png", height=210)


#loading data and important metrics

df = pd.read_csv('Database.csv')
number_of_entries = len(df)

productivity_metrics = im.ImportantMetrics(metric_list = [ 'Weight', 'Body-Fat %', 'VO2 Max', 'Net Calories', 'Steps', 'Active Cals', 'Total Cals', 'Exercise' , 'Cals Consumed', 'Protein', 'Carbs', 'Fat', 'Saturated Fat', 'Sugar', 'Sleep'])
yesterdays_metrics = productivity_metrics.get_time_period_metric(1)
yesterday_vs_day_before_yesterday_percent_change = productivity_metrics.get_time_period_percent_change(1)
three_day_averages = productivity_metrics.get_time_period_metric(3)
current_three_day_vs_past_three_day = productivity_metrics.get_time_period_percent_change(3)
seven_day_averages = productivity_metrics.get_time_period_metric(7)
current_seven_day_vs_past_seven_day = productivity_metrics.get_time_period_percent_change(7)


# sidebar

with st.sidebar:
    st.markdown("<h4 style='text-align: center;color: #FDF4DC;'>Date Range Slider</t>", unsafe_allow_html=True)
    date_range = st.select_slider(label = 'DATE RANGE SLIDER', options = ['Yesterday', '3 Day Average', '7 Day Average'], label_visibility = 'collapsed')

import streamlit.components.v1 as com

com.html(html='''<!DOCTYPE html>

    </head>
    <body>
        <h1> Gabriella Martin - SUCK MY PUSSYHOLE LAUREN SACK OF SHIT </h1 >
        <p><em>Hello suck my pusy</em></p>
        <p>I am a developer I love <a href="appbrewery.co">coffee</a></p>
        <hr>
        <h3>Projects</h3>
        <ul></ul>
            <li>yaaaa</li>
            <li> <a href="lauren.html">shutup</a>  </li>
            <ol type='i'>
                <li><a href="www.google.com">lauren is an ogre</a> </li>
                <img src="data:image/jpeg;base64,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" alt="dog">
            </ol>
    </body>
''')






# start of visual

st.markdown("<h1 style='text-align: center;color: #FDF4DC;'>Health Hub</h1>", unsafe_allow_html=True)


st.markdown(f"<a  href='#linkto_data' style='color: #FDF4DC;'>💡Click here for data details</a>", unsafe_allow_html=True)

st.write('')
columns = st.columns(5)
with columns[0]:
    st.write('')
    st.write('')
    st.write('#### Overall :')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('#### Activity : ')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('#### Nutrition :')


with columns[1]:
    if date_range == '3 Day Average':
            st.metric(label='Weight kg', value=three_day_averages[0], delta=str(current_three_day_vs_past_three_day[0]) + '%', delta_color='inverse')
            st.metric(label='Steps', value = three_day_averages[4], delta=str(current_three_day_vs_past_three_day[4]) + '%')
            st.metric(label='Cals Consumed', value=three_day_averages[8], delta=str(current_three_day_vs_past_three_day[8]) + '%', delta_color='inverse')
    if date_range == '7 Day Average':
            st.metric(label='Weight kg', value=seven_day_averages[0], delta=str(current_seven_day_vs_past_seven_day[0]) + '%', delta_color='inverse')
            st.metric(label='Steps', value = seven_day_averages[4], delta=str(current_seven_day_vs_past_seven_day[4])+ '%')  
            st.metric(label='Cals Consumed', value=seven_day_averages[8], delta=str(current_seven_day_vs_past_seven_day[8]) + '%', delta_color='inverse')
    if date_range == 'Yesterday':
            st.metric(label='Weight kg', value=yesterdays_metrics[0], delta=str(yesterday_vs_day_before_yesterday_percent_change[0]) + '%', delta_color='inverse')
            st.metric(label='Steps', value=yesterdays_metrics[4], delta=str(yesterday_vs_day_before_yesterday_percent_change[4]) + '%')
            st.metric(label='Cals Consumed', value=yesterdays_metrics[8], delta=str(yesterday_vs_day_before_yesterday_percent_change[8]) + '%', delta_color='inverse')


with columns[2]:
    if date_range == '3 Day Average':
            
            st.metric(label='Body-Fat %', value=three_day_averages[1], delta=str(current_three_day_vs_past_three_day[1]) + '%', delta_color='inverse')
            st.metric(label='Active Cals', value=three_day_averages[5], delta=str(current_three_day_vs_past_three_day[5]) + '%')
            st.metric(label='Protein g', value=three_day_averages[9])
            
    if date_range == '7 Day Average':
            st.metric(label='Body-Fat %', value=seven_day_averages[1], delta=str(current_seven_day_vs_past_seven_day[1]) + '%', delta_color='inverse')
            st.metric(label='Active Cals', value=seven_day_averages[5], delta=str(current_seven_day_vs_past_seven_day[5]) + '%')
            st.metric(label = 'Protein g', value=seven_day_averages[9])


    if date_range == 'Yesterday':
            
            st.metric(label='Body-Fat %', value=yesterdays_metrics[1], delta=str(yesterday_vs_day_before_yesterday_percent_change[1]) + '%', delta_color='inverse')
            st.metric(label='Active Cals', value=yesterdays_metrics[5], delta=str(yesterday_vs_day_before_yesterday_percent_change[5]) + '%')
            st.metric(label='Protein g',value = yesterdays_metrics[9])



with columns[3]:
    if date_range == '3 Day Average':
            
            st.metric(label='V0₂ Max', value=three_day_averages[2], delta=str(current_three_day_vs_past_three_day[2]) + '%')
            st.metric(label='Total Cals', value=three_day_averages[6], delta=str(current_three_day_vs_past_three_day[6]) + '%')
            st.metric(label='Fat g', value = three_day_averages[11])
            #st.metric(label='Saturated Fat g', value = three_day_averages[12])
            
    if date_range == '7 Day Average':
            st.metric(label='V0₂ Max', value=seven_day_averages[2], delta=str(current_seven_day_vs_past_seven_day[2]) + '%')
            st.metric(label='Total Cals', value=seven_day_averages[6], delta=str(current_seven_day_vs_past_seven_day[6]) + '%')
            st.metric(label='Fat g', value = seven_day_averages[11])
            #st.metric(label='Saturated Fat g', value=seven_day_averages[12])
    if date_range == 'Yesterday':
            
            st.metric(label='V0₂ Max', value=yesterdays_metrics[2], delta=str(yesterday_vs_day_before_yesterday_percent_change[2]) + '%')
            st.metric(label='Total Cals', value=yesterdays_metrics[6], delta=str(yesterday_vs_day_before_yesterday_percent_change[6]) + '%')
            st.metric(label='Fat g', value = yesterdays_metrics[11])
            #st.metric(label='Saturated Fat g', value = yesterdays_metrics[12])
with columns[4]:
    if date_range == '3 Day Average':
            
            st.metric(label='Net Calories', value=three_day_averages[3], delta=str(current_three_day_vs_past_three_day[3]) + '%', delta_color='inverse')
            st.metric(label='Exercise Mins', value=three_day_averages[7], delta=str(current_three_day_vs_past_three_day[7]) + '%')

    if date_range == '7 Day Average':
            
            st.metric(label='Net Calories', value=seven_day_averages[3], delta=str(current_seven_day_vs_past_seven_day[3]) + '%', delta_color='inverse')
            st.metric(label='Exercise Mins', value=seven_day_averages[7], delta=str(current_seven_day_vs_past_seven_day[7]) + '%')

    if date_range == 'Yesterday':
            st.metric(label='Net Calories', value=yesterdays_metrics[3], delta=str(yesterday_vs_day_before_yesterday_percent_change[3]) + '%', delta_color='inverse')
            st.metric(label='Exercise Mins', value=yesterdays_metrics[7], delta = str(yesterday_vs_day_before_yesterday_percent_change[7])+ '%')


    if date_range == '3 Day Average':
        st.metric(label='Carbs g', value = three_day_averages[10])
        #st.metric(label='Sugar g', value = three_day_averages[13])
        
        
    if date_range == '7 Day Average':
        st.metric(label='Carbs g', value = seven_day_averages[10])
        #st.metric(label='Sugar g', value = seven_day_averages[13])
        
    if date_range == 'Yesterday':
        st.metric(label='Carbs g', value = yesterdays_metrics[10])
        #st.metric(label='Sugar g', value = yesterdays_metrics[13])

# line graph of long term data
st.write('')
st.write('')
col1, col2, col3, col4 = st.columns([3,3, 2, 4])

with col1:
    labels = ['Protein', 'Carbs', 'Fat']
    if date_range == 'Yesterday':
        values = [yesterdays_metrics[9], yesterdays_metrics[10], yesterdays_metrics[11]]
        
    if date_range == '3 Day Average':
        values = [three_day_averages[9], three_day_averages[10], three_day_averages[11]]
    
    if date_range == '7 Day Average':
        values = [seven_day_averages[9], seven_day_averages[10], seven_day_averages[11]]
    fig = px.pie( title = 'Yesterday:',height = 290, values=values, labels=labels, width=250, names=labels, hole=0.7, color = labels, color_discrete_map={'Protein':'#6e6056', 'Carbs': '#a69a8f', 'Fat': '	#e5ddd3'})
    st.plotly_chart(fig)

with col2:
        
        labels = ['Protein', 'Carbs', 'Fat']
        values = [50, 20, 30]

        fig = px.pie(title = 'Goal:',height = 290, names = labels, values=values, labels=labels, width=250,  hole=0.7, color = labels, color_discrete_map={'Protein':'#6e6056', 'Carbs': '#a69a8f', 'Fat': '#e5ddd3'})

        st.plotly_chart(fig)

with col4:
    st.write('')
    if date_range == '3 Day Average':
        st.write(f'## Sleep: {three_day_averages[14]}hrs')
    if date_range == '7 Day Average':
        st.write(f'## Sleep: {seven_day_averages[14]}hrs')
    if date_range == 'Yesterday':
        st.write(f'## Sleep: {yesterdays_metrics[14]}hrs')
    st.write('')
    with st.expander('**Daily Goals**', expanded=False):
        
        st.write('10,000 Steps' +'  \n' + '550 Active Cals' +'  \n' + '5 Diet Score' +'  \n' + 'Deficit: Cutting Phase')
    
    with st.expander('**Long-Term Goals**', expanded=False):
        st.markdown('15% Body Fat' +'  \n' + 'High VO<sub>2</sub>  Max' , unsafe_allow_html=True)


selected = pills("What to visualise", [ "Diet", "Steps", 'Active Cals', 'Total Cals', 'VO2 Max', 'Weight', 'Body-Fat %', 'Net Calories', 'Sleep'], 
[ "🥗", '🚶🏽‍♀️', '🔋', '⚡', '🫀', '⚖️','📉', '🥅','💤' ], label_visibility='collapsed')


if selected == 'Health' or selected == 'Steps Score' or selected == 'Active Cals Score' or selected == 'Diet':
    fig = px.line(df, x='Days', y =[selected], color_discrete_sequence=["#6e6056", "#e5ddd3"])
    fig.update(layout_yaxis_range = [50,130])
    st.plotly_chart(fig, use_container_width=True)

else:
    fig = px.line(df, x='Days', y =selected, color_discrete_sequence= ["#6e6056"])
    st.plotly_chart(fig, use_container_width=True)  

st.markdown(f"<div id='linkto_data'></div>", unsafe_allow_html=True)
data = st.write('')
# behind the scenes
with st.expander(label='Behind the Scenes', expanded=True):
    st.write('')
    with st.expander(label='Data Pipeline'):

        st.write('**The full code for my health pipeline can be viewed [here]( https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/Pipelines/Health-Data-Pipeline.py)**')
        st.write('### • Retrieving Steps, Active Calories, Total Calories Burned, Exercise, VO₂ Max & Diet')
        st.write('')
        cols = st.columns([0.2,6,0.2])
        cols[1].write("My apple watch tracks my movement and VO2 max but currently there is no easy direct access to automatically retrieve this data, so I figured a work-around. Starting with [this app](https://www.healthexportapp.com/) and an iOS Shortcut that runs once daily at night that aggregates and retrieves important data points and saves it to a CSV in my iCloud Drive I use [MyFitnessPal](https://www.myfitnesspal.com/) to track my diet. Although they have their own [API](https://myfitnesspalapi.com/), they are selective of who they give out API keys to, I have applied but have yet to receive a response. Nevertheless, Apple Health can connect to it for some basic metrics which is sufficient for my needs. I chose the most important diet metrics to me and included these in the daily data extraction")
        st.write('')
        st.write('')
        with cols[1]:
            inner_cols = st.columns(2)
            inner_cols[0].image(image = 'images/automatingshortcut.PNG')
            inner_cols[1].write('')
            inner_cols[1].image(image = 'images/shortcut.PNG')

        cols = st.columns([0.2,6,0.2])
        cols[1].write('Next step is to gain access to this file in my Python script, for this I use [PyiCloud]( https://github.com/picklepete/pyicloud). Once the file is accessible, I use python to extract and process the data. This data alongside the other health metrics is then added to my database CSV file ready to be visualised here with Pandas')
        st.write('')

        st.write('### • Retrieving Sleep')
        cols = st.columns([0.2,6,0.2])
        cols[1].write('Although in theory the above process should work for sleep data, I found it buggy - 50% of the time the sleep data was empty. However, what I use for my [mood-tracker]( https://exist.io/) has integrations with Apple Health, so getting sleep from their [API]( https://developer.exist.io/) was much more successful. I run my python script each night, I use their REST API to get my sleep time, which goes directly to my CSV ready for visualisation here with Pandas')

        st.write('### • Retrieving Body Metrics')
        cols = st.columns([0.2,6,0.2])
        cols[1].write('For retrieval of my body measurements, I use a [Withings Smart-Scale]( https://www.withings.com/uk/en/scales), coupled with their [API]( https://developer.withings.co.uk/). I do a daily weigh-in which my Python script calls daily. The data is then added to my CSV database for visualisation with Pandas')
        st.write('')
        st.write('')

    with st.expander(label='Visualisation'):
        Visuals.health_visual()
    
    with st.expander(label='Future Roadmap'):
        st.write('wger, strava, google maps')


# section with pie charts


