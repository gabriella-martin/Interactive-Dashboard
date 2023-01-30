
import streamlit as st
from streamlit_extras.app_logo import add_logo
add_logo("logo_white_background.jpg", height=150)

import plotly.express as px
import pandas as pd

df = pd.read_csv('Database.csv')



number_of_entries = len(df)
from streamlit_extras.metric_cards import style_metric_cards
#style_metric_cards( border_left_color='#ff4bd0')

style_metric_cards( border_left_color='#6F4E37', border_size_px =2, border_color='#ccbea3', border_radius_px=10)
from streamlit_extras.stoggle import stoggle
st.markdown("<h3 style='text-align: center;color: black;'>Personal</h3>", unsafe_allow_html=True)



# yesterday
st.markdown("<h4 style='text-align: center;color: black;'>Short Term</h4>", unsafe_allow_html=True)


import important_metrics as im
productivity_metrics = im.ImportantMetrics(metric_list = ['Personal', 'Dogs', 'Cleaning', 'Self-Care'])
yesterdays_metrics = productivity_metrics.get_yesterdays_metrics()
yesterday_vs_day_before_yesterday_percent_change = productivity_metrics.get_yesterday_percentage_change()
three_day_averages = productivity_metrics.get_three_day_averages()
current_three_day_vs_past_three_day = productivity_metrics.get_three_day_percentage_change()
seven_day_averages = productivity_metrics.get_seven_day_averages()
current_seven_day_vs_past_seven_day = productivity_metrics.get_seven_day_percentage_change()

    
date_range = st.select_slider(label = 'What date range would you like to see?', options = ['Yesterday', '3 Days', '7 Days'], label_visibility = 'collapsed')

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



st.markdown("<h4 style='text-align: center;color: black;'>Long Term</h4>", unsafe_allow_html=True)

select = st.multiselect(label = '', options =  ['Personal', 'Dogs', 'Cleaning', 'Self-Care', 'Goal Score'], default=['Personal', 'Goal Score'], label_visibility = 'collapsed')


fig = px.line(df, x='Days', y=select, color_discrete_sequence=[ "pink", "hotpink", "deeppink"])
fig.update(layout_yaxis_range = [50,120])
fig.update_layout( xaxis_title = 'Day', yaxis_title = 'Score')

st.plotly_chart(fig)
