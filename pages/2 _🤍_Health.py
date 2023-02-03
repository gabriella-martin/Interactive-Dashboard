
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

color = '#6e6056'

style_metric_cards( background_color = color,border_left_color=color, border_size_px =0.3, border_color=color, border_radius_px=10)
add_logo("logo_transparent_background.png", height=160)


#loading data and important metrics


df = pd.read_csv('Database.csv')
number_of_entries = len(df)

productivity_metrics = im.ImportantMetrics(metric_list = ['Health', 'Steps Score', 'Active Cals Score', 'Diet', 'Goal Score', 'Weight', 'Body-Fat %'])
yesterdays_metrics = productivity_metrics.get_time_period_metric(1)
yesterday_vs_day_before_yesterday_percent_change = productivity_metrics.get_time_period_percent_change(1)
three_day_averages = productivity_metrics.get_time_period_metric(3)
current_three_day_vs_past_three_day = productivity_metrics.get_time_period_percent_change(3)
seven_day_averages = productivity_metrics.get_time_period_metric(7)
current_seven_day_vs_past_seven_day = productivity_metrics.get_time_period_percent_change(7)


# start of visual


st.markdown("<h1 style='text-align: center;color: #FDF4DC;'>Health Hub</h1>", unsafe_allow_html=True)

st.write('')


# first section 


date_range = st.select_slider(label = 'What date range would you like to see?', options = ['Yesterday', '3 Days', '7 Days'], label_visibility = 'collapsed')
outer_cols = st.columns([6, 0.5, 1.3,1.3])

with outer_cols[0]:
    
    col1, col2, col3, col4 = st.columns([1.5,1.5,1.5,1.5])
    
    if date_range == '3 Days':
        
        col1.metric(label="Health", value=three_day_averages[0], delta=str(current_three_day_vs_past_three_day[0]) + '%')
        col2.metric(label="Steps", value=three_day_averages[1], delta=str(current_three_day_vs_past_three_day[1]) + '%')
        col3.metric(label="Active Cals", value=three_day_averages[2], delta=str(current_three_day_vs_past_three_day[2]) + '%')
        col4.metric(label="Diet", value=three_day_averages[3], delta=str(current_three_day_vs_past_three_day[3]) + '%')

    if date_range == '7 Days':
        
        col1.metric(label="Health", value=seven_day_averages[0], delta=str(current_seven_day_vs_past_seven_day[0]) + '%')
        col2.metric(label="Steps", value=seven_day_averages[1], delta=str(current_seven_day_vs_past_seven_day[1]) + '%')
        col3.metric(label="Active Cals", value=seven_day_averages[2], delta=str(current_seven_day_vs_past_seven_day[2]) + '%')
        col4.metric(label="Diet", value=seven_day_averages[3], delta=str(current_seven_day_vs_past_seven_day[3]) + '%')

    if date_range == 'Yesterday':
        
        col1.metric(label="Health", value=yesterdays_metrics[0], delta=str(yesterday_vs_day_before_yesterday_percent_change[0]) + '%')
        col2.metric(label="Steps", value=yesterdays_metrics[1], delta=str(yesterday_vs_day_before_yesterday_percent_change[1]) + '%')
        col3.metric(label="Active Cals", value=yesterdays_metrics[2], delta=str(yesterday_vs_day_before_yesterday_percent_change[2]) + '%')
        col4.metric(label="Diet", value=yesterdays_metrics[3], delta=str(yesterday_vs_day_before_yesterday_percent_change[3]) + '%')

with outer_cols[2]:

    if date_range == '3 Days':
       
        st.metric(label='Weight', value=three_day_averages[5], delta=str(current_three_day_vs_past_three_day[5]) + '%', delta_color='inverse')
    if date_range == '7 Days':
        
        st.metric(label='Weight', value=seven_day_averages[5], delta=str(current_seven_day_vs_past_seven_day[5]) + '%', delta_color='inverse')
    if date_range == 'Yesterday':
        
        st.metric(label='Weight', value=yesterdays_metrics[5], delta=str(yesterday_vs_day_before_yesterday_percent_change[5]) + '%', delta_color='inverse')

with outer_cols[3]:

    if date_range == '3 Days':
        
        st.metric(label='Body-Fat%', value=three_day_averages[6], delta=str(current_three_day_vs_past_three_day[6]) + '%', delta_color='inverse')
    if date_range == '7 Days':
        
        st.metric(label='Body-Fat%', value=seven_day_averages[6], delta=str(current_seven_day_vs_past_seven_day[6]) + '%', delta_color='inverse')
    if date_range == 'Yesterday':
        
        st.metric(label='Body-Fat%', value=yesterdays_metrics[6], delta=str(yesterday_vs_day_before_yesterday_percent_change[6]) + '%', delta_color='inverse')


# section with pie charts


col1, col2, col3, col4 = st.columns([3,3, 2, 4])

with col1:
        labels = ['Protein', 'Carbs', 'Fat']
        values = [120, 60, 40]

        fig = px.pie( title = 'Yesterday:',height = 290, values=values, labels=labels, width=250, names=labels, hole=0.7, color = labels, color_discrete_map={'Protein':'#6e6056', 'Carbs': '#a69a8f', 'Fat': '	#e5ddd3'})
#FFBCC3
        st.plotly_chart(fig)

with col2:
        
        labels = ['Protein', 'Carbs', 'Fat']
        values = [50, 20, 30]

        fig = px.pie(title = 'Goal:',height = 290, names = labels, values=values, labels=labels, width=250,  hole=0.7, color = labels, color_discrete_map={'Protein':'#6e6056', 'Carbs': '#a69a8f', 'Fat': '#e5ddd3'})

        st.plotly_chart(fig)

with col4:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    
    with st.expander('**Daily Goals**', expanded=False):
        
        st.write('10,000 Steps' +'  \n' + '550 Active Cals' +'  \n' + '5 Diet Score' +'  \n' + 'Deficit: Cutting Phase')
    
    with st.expander('**Long-Term Goals**', expanded=False):
        st.markdown('15% Body Fat' +'  \n' + 'High VO<sub>2</sub>  Max' , unsafe_allow_html=True)


# line graph of long term data


selected = pills("What to visualise", ["Health", "Steps Score", "Active Cals Score", "Diet", "Steps", 'Active Cals', 'Total Cals Burned', 'VO2 Max', 'Weight', 'Body-Fat %', 'Net Calories', 'Sleep'], ["💪🏾", "🚶🏽‍♀️", "🔋", "🥗", '🚶🏽‍♀️', '🔋', '⚡', '🫀', '⚖️','📉', '🥅', '💤' ], label_visibility='collapsed')


if selected == 'Health' or selected == 'Steps Score' or selected == 'Active Cals Score' or selected == 'Diet':
    fig = px.line(df, x='Days', y =[selected, 'Goal Score'], color_discrete_sequence=["#6e6056", "#e5ddd3"])
    fig.update(layout_yaxis_range = [50,130])
    st.plotly_chart(fig, use_container_width=True)

else:
    fig = px.line(df, x='Days', y =selected, color_discrete_sequence= ["#6e6056"])
    st.plotly_chart(fig, use_container_width=True)  


# behind the scenes


with st.expander('**Behind The Scenes**', expanded=False):
        
    with st.expander('**Data Details**', expanded=False):
        st.write('')

    with st.expander('**Data Pipeline**', expanded=False):
        Visuals.health_visual()

    with st.expander('**Future Roadmap**', expanded=False):
        st.write('wger, strava, google maps')
    st.write('axis')