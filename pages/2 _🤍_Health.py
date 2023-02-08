
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
add_logo("logo_transparent_background.png", height=210)


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
            inner_cols[0].image(image = 'images/automatingshortcut.png')
            inner_cols[1].write('')
            inner_cols[1].image(image = 'images/shortcut.png')

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


