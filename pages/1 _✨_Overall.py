# streamlit run Streamlit.py

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.let_it_rain import rain
from datetime import datetime
import json
import random
import plotly.graph_objects as go
from streamlit_echarts import st_echarts
from streamlit_extras.app_logo import add_logo
import requests
from decouple import config
add_logo("missmartin.jpeg", height=150)






style_metric_cards( border_left_color='#ff4bd0')

df = pd.read_csv('Database.csv')
number_of_entries = len(df)

quote_list = [ "Do one small thing to make today better than yesterday", "I may not be there yet, but I’m closer than I was yesterday",
"I wake up every morning believing today is going to be better than yesterday", "Make the work you are doing today better than the work you did yesterday",
"Be better today than you were yesterday, and be better tomorrow than you are today", "Be your biggest competitor – challenge yourself each day to be better than you were yesterday"
,"All we can do is be better prepared today than yesterday and better prepared tomorrow than today", "The beautiful thing about today is that you get the choice to make it better than yesterday”, “Above all, I strive to be the best I can, to be better than I was yesterday and better tomorrow",
"If you make it a habit to make your today better than your yesterday, then for sure, your tomorrow will be better than your today", "That morning she feels fresh-scrubbed and cleansed, as if she is being given yet another opportunity to live her life correctly"]  

quote = random.choice(quote_list)

st.write('## Overall')

st.markdown("<h3 style='text-align: center;color: black;'>Short Term</h3>", unsafe_allow_html=True)
st.write(f'>{quote}')

metric_list = ['Overall', 'Health', 'Productivity', 'Personal']
yesterdays_metrics = []

def get_yesterdays_metric(metric_list):
    for i in metric_list:
        yesterday_metric = df.iloc[number_of_entries -1][i]
        yesterdays_metrics.append(yesterday_metric)
    return yesterdays_metrics

yesterdays_metrics = get_yesterdays_metric(metric_list)
yesterday_vs_day_before_yesterday_percent_change = []

def get_percentage_change(metric_list, yesterdays_metrics):
    for index, value in enumerate(yesterdays_metrics):
        percent_change = round((((value - (df.iloc[number_of_entries-2])[metric_list[index]]))/((df.iloc[number_of_entries-2])[metric_list[index]]))*100)
        yesterday_vs_day_before_yesterday_percent_change.append(percent_change)
    return yesterday_vs_day_before_yesterday_percent_change

yesterday_vs_day_before_yesterday_percent_change = get_percentage_change(metric_list, yesterdays_metrics)

def get_three_day_average():
  three_day_averages = []
  for category in metric_list:
    yesterday_metric = df.iloc[number_of_entries -1][category]
    yesterday_minusone_metric = df.iloc[number_of_entries -2][category]
    yesterday_minustwo_metric = df.iloc[number_of_entries -3][category]
    three_day_average =round((yesterday_metric + yesterday_minusone_metric + yesterday_minustwo_metric)/3)
    three_day_averages.append(three_day_average)
  return three_day_averages

three_day_averages = get_three_day_average()
current_three_day_vs_past_three_day = []
three_day_percent_change = []

def get_percentage_change(metric_list, three_day_averages):
    for index, value in enumerate(three_day_averages):
        three_day_earlier_average = ((((df.iloc[number_of_entries-4])[metric_list[index]]) + (df.iloc[number_of_entries-5][metric_list[index]]) + (df.iloc[number_of_entries-6])[metric_list[index]]))/3
        percent_change = round((((value - three_day_earlier_average))/three_day_earlier_average)*100)
        current_three_day_vs_past_three_day.append(percent_change)
    return current_three_day_vs_past_three_day
    
current_three_day_vs_past_three_day = get_percentage_change(metric_list, three_day_averages)
    
def get_seven_day_metric():
    seven_day_averages = []
    for category in metric_list:
        yesterday_metric = df.iloc[number_of_entries -1][category]
        yesterday_minusone_metric = df.iloc[number_of_entries -2][category]
        yesterday_minustwo_metric = df.iloc[number_of_entries -3][category]
        yesterday_minusthree_metric = df.iloc[number_of_entries -4][category]
        yesterday_minusfour_metric = df.iloc[number_of_entries -5][category]
        yesterday_minusfive_metric = df.iloc[number_of_entries -6][category]
        yesterday_minussix_metric = df.iloc[number_of_entries -7][category]
        seven_day_average =round((yesterday_metric + yesterday_minusone_metric + yesterday_minustwo_metric  + yesterday_minusthree_metric +
        yesterday_minusfour_metric + yesterday_minusfive_metric + yesterday_minussix_metric )/7)
        seven_day_averages.append(seven_day_average)
    return seven_day_averages

seven_day_averages = get_seven_day_metric()
current_seven_day_vs_past_seven_day = []
seven_day_percent_change = []

def get_percentage_change(metric_list, seven_day_averages):
    for index, value in enumerate(seven_day_averages):
        seven_day_earlier_average = ((((df.iloc[number_of_entries-8])[metric_list[index]]) + (df.iloc[number_of_entries-9][metric_list[index]]) + (df.iloc[number_of_entries-10])[metric_list[index]]) + 
        (df.iloc[number_of_entries-11][metric_list[index]]) + (df.iloc[number_of_entries-12][metric_list[index]]) + (df.iloc[number_of_entries-13][metric_list[index]]) + (df.iloc[number_of_entries-14][metric_list[index]]) )/7
        percent_change = round((((value - seven_day_earlier_average))/seven_day_earlier_average)*100)
        current_seven_day_vs_past_seven_day.append(percent_change)
    return current_seven_day_vs_past_seven_day
    
current_seven_day_vs_past_seven_day = get_percentage_change(metric_list, seven_day_averages)
    
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
  style_metric_cards( border_left_color='#ff4bd0')

  if yesterdays_metrics[0] >= 100:
    rain(emoji="🎯",font_size=54,falling_speed=5,animation_length="5")
    st.success('Congratulations, yesterday you hit your goal score!', icon='🎯')
    
  if yesterdays_metrics[0] <100 and yesterdays_metrics[0] >95:
    rain(emoji="⚠️",font_size=54,falling_speed=5,animation_length="5")
    st.warning('So close! You nearly hit your target, try better today!', icon="⚠️")
    
  if yesterdays_metrics[0] <=95:
    rain(emoji="🚨",font_size=54,falling_speed=5,animation_length="5")
    st.error('Yesterday you were off track, try extra hard today!', icon='🚨')
  











st.markdown("<h3 style='text-align: center;color: black;'>Long Term</h3>", unsafe_allow_html=True)



select = st.multiselect('What do you want to visualise?', ['Overall', 'Health', 'Productivity', 'Personal', 'Goal Score'], default =['Goal Score', 'Overall'])

fig = px.line(df, x='Days', y=select, color_discrete_sequence=[ "pink", "hotpink", "deeppink",  'plum', 'darkmagenta'])
fig.update(layout_yaxis_range = [60,120])

st.plotly_chart(fig)

st.markdown("<h3 style='text-align: center;color: black;'>Heatmaps</h3>", unsafe_allow_html=True)

select = st.selectbox(label ='What heatmap do you want to visualise?', options=['Overall', 'Health', 'Productivity', 'Personal'])



z = df[select]
x = df['Month']
y = df['Day of Month']
heatmap = go.Figure([go.Heatmap(z=z, x=x, y=y, colorscale=[[0, '#fcfafc'],[1, '#fc03bb']])])
heatmap.update_layout( xaxis_title = 'Month', yaxis_title = 'Day of Month')

st.plotly_chart(heatmap)

st.markdown("<h3 style='text-align: center;color: black;'>Boxplots</h3>", unsafe_allow_html=True)
select = st.selectbox(label ='What boxplot do you want to visualise?', options=['Overall', 'Health', 'Productivity', 'Personal'])

fig = px.box(df, x='Month', y=select, color_discrete_sequence=[ "hotpink"])


st.plotly_chart(fig)


