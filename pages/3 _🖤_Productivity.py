# github yesterday commits
import streamlit as st
from streamlit_extras.app_logo import add_logo
add_logo("logo_white_background.jpg", height=150)
import pandas as pd
import plotly.express as px

df = pd.read_csv('Database.csv')
number_of_entries = len(df)
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.stoggle import stoggle

st.markdown("<h1 style='text-align: center;color: black;'>Productivity Hub</h1>", unsafe_allow_html=True)

# yesterday


import streamlit_nested_layout









metric_list = ['Productivity', 'Work Score', 'Reading Score']

import importlib 
DataPipeline = importlib.import_module('Data-Pipeline')

a=DataPipeline.AirTablePipeline()
currently_reading = a.get_currently_reading_books()



import important_metrics as im
productivity_metrics = im.ImportantMetrics(metric_list = ['Productivity', 'Work Score', 'Reading Score', 'GitHub Contributions', 'Coding Time Decimal'])
yesterdays_metrics = productivity_metrics.get_yesterdays_metrics()
yesterday_vs_day_before_yesterday_percent_change = productivity_metrics.get_yesterday_percentage_change()
three_day_averages = productivity_metrics.get_three_day_averages()
current_three_day_vs_past_three_day = productivity_metrics.get_three_day_percentage_change()
seven_day_averages = productivity_metrics.get_seven_day_averages()
current_seven_day_vs_past_seven_day = productivity_metrics.get_seven_day_percentage_change()

# move to exist pipeline backend 


yesterdays_streak = df.iloc[number_of_entries -1]['GitHub Streak']


outer_cols = st.columns([6,0.8,3])


with outer_cols[0]:
    date_range = st.select_slider(label = 'What date range would you like to see?', options = ['Yesterday', '3 Days', '7 Days'], label_visibility = 'collapsed', key=1)
    if date_range == '3 Days':
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Productivity", value=three_day_averages[0], delta=str(current_three_day_vs_past_three_day[0]) + '%')
        col2.metric(label="Work Score", value=three_day_averages[1], delta=str(current_three_day_vs_past_three_day[1]) + '%')
        col3.metric(label="Reading Score", value=three_day_averages[2], delta=str(current_three_day_vs_past_three_day[2]) + '%')

    if date_range == '7 Days':
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Productivity", value=seven_day_averages[0], delta=str(current_seven_day_vs_past_seven_day[0]) + '%')
        col2.metric(label="Work Score", value=seven_day_averages[1], delta=str(current_seven_day_vs_past_seven_day[1]) + '%')
        col3.metric(label="Reading Score", value=seven_day_averages[2], delta=str(current_seven_day_vs_past_seven_day[2]) + '%')

    if date_range == 'Yesterday':
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Productivity", value=yesterdays_metrics[0], delta=str(yesterday_vs_day_before_yesterday_percent_change[0]) + '%')
        col2.metric(label="Work Score", value=yesterdays_metrics[1], delta=str(yesterday_vs_day_before_yesterday_percent_change[1]) + '%')
        col3.metric(label="Reading Score", value=yesterdays_metrics[2], delta=str(yesterday_vs_day_before_yesterday_percent_change[2]) + '%')
    #score graph

with outer_cols[2]:
    st.write('')


    with st.expander('**📖 Currently Reading**', expanded=False):
    
        col1,col2,col3= st.columns(3)

        with col1:
        
            st.image(image=currently_reading[0][0], use_column_width='always')
            st.write(currently_reading[1][0] + '%')


        with col2:
        
            st.image(image=currently_reading[0][1], use_column_width='always')
            st.write(currently_reading[1][1] + '%')
        with col3:
        
            st.image(image=currently_reading[0][2], use_column_width='always')
            st.write(currently_reading[1][2] + '%')
           
    with st.expander('**😺🐙 GitHub Statistics**', expanded=False):
        if date_range == '3 Days':
            col1, col2 = st.columns(2)
            col1.metric(label="Commits", value=three_day_averages[3], delta=str(current_three_day_vs_past_three_day[3]) + '%')

        if date_range == '7 Days':
            col1, col2 = st.columns(2)
            col1.metric(label="Commits", value=seven_day_averages[3], delta=str(current_seven_day_vs_past_seven_day[3]) + '%')


        if date_range == 'Yesterday':
            col1, col2 = st.columns(2)
            col1.metric(label="Commits", value=yesterdays_metrics[3], delta=str(yesterday_vs_day_before_yesterday_percent_change[3]) + '%')

    
        col2.write('')
        col2.metric(label='Streak', value = yesterdays_streak)

    with st.expander('**💻 Coding Statistics**', expanded=False):
        # change to nice format for display digital clock
        if date_range == '3 Days':
            
            st.metric(label="Hours", value=three_day_averages[4], delta=str(current_three_day_vs_past_three_day[4]) + '%')

        if date_range == '7 Days':
            
            st.metric(label="Hours", value=seven_day_averages[4], delta=str(current_seven_day_vs_past_seven_day[4]) + '%')


        if date_range == 'Yesterday':
            
            st.metric(label="Hours", value=yesterdays_metrics[4], delta=str(yesterday_vs_day_before_yesterday_percent_change[4]) + '%')

    
     

style_metric_cards( border_left_color='#6F4E37', border_size_px =2, border_color='#ccbea3', border_radius_px=10)
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

 












st.markdown("<h4 style='text-align: center;color: black;'>Long Term</h4>", unsafe_allow_html=True)
data_type = st.radio(label = '', options = ['Score Adjusted Data', 'Raw Data'], horizontal = True, label_visibility = 'collapsed')

if data_type == 'Score Adjusted Data':
    select = st.multiselect(label = '', options = ['Productivity', 'Work Score', 'Reading Score', 'Goal Score'], default=['Productivity', 'Goal Score'], label_visibility = 'collapsed')


    fig = px.line(df, x='Days', y=select, color_discrete_sequence=[ "pink", "hotpink", "deeppink"])
    fig.update(layout_yaxis_range = [50,120])
    fig.update_layout( xaxis_title = 'Day', yaxis_title = 'Score')

    st.plotly_chart(fig)

if data_type == 'Raw Data':
#raw data


    select_raw = st.selectbox(label = '', options=[ 'Work Hours', 'Reading Hours'], label_visibility='collapsed')

    if select_raw == 'Work Hours':
        figure = px.line(df, x='Days', y=['Work Hours', 'Work Hours Goal'] , color_discrete_sequence=[ "pink", "hotpink"])
        figure.update(layout_yaxis_range = [0,14])
        figure.update_layout( xaxis_title = 'Day', yaxis_title = 'Hours')
        st.plotly_chart(figure)
        


    if select_raw == 'Reading Hours':
        figure = px.line(df, x='Days', y=['Reading Hours', 'Reading Hours Goal'], color_discrete_sequence=[  "pink", "hotpink"])
        figure.update(layout_yaxis_range = [-5,6])
        figure.update_layout( xaxis_title = 'Day', yaxis_title = 'Hours')
        st.plotly_chart(figure)


