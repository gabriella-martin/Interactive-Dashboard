# streamlit run Streamlit.py

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.let_it_rain import rain

import json
from streamlit_echarts import st_echarts
from streamlit_extras.app_logo import add_logo
add_logo("missmartin.jpeg", height=150)

df = pd.read_csv('Database.csv')
number_of_entries = len(df)

st.write("### Yesterday's Metrics")
st.write('>Quote about better than yesterday')

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

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Overall", value=yesterdays_metrics[0], delta=str(yesterday_vs_day_before_yesterday_percent_change[0]) + '%')
col2.metric(label="Health", value=yesterdays_metrics[1], delta=str(yesterday_vs_day_before_yesterday_percent_change[1]) + '%')
col3.metric(label="Productivity", value=yesterdays_metrics[2], delta=str(yesterday_vs_day_before_yesterday_percent_change[2]) + '%')
col4.metric(label="Personal", value=yesterdays_metrics[3], delta=str(yesterday_vs_day_before_yesterday_percent_change[3]) + '%')
style_metric_cards( border_left_color='#ff4bd0')

# github yesterday commits
if yesterdays_metrics[0] >= 100:
  rain(emoji="🎯",font_size=54,falling_speed=5,animation_length="5")
  st.success('Congratulations, yesterday you hit your goal score!', icon='🎯')
  
if yesterdays_metrics[0] <100 and yesterdays_metrics[0] >95:
  rain(emoji="⚠️",font_size=54,falling_speed=5,animation_length="5")
  st.warning('So close! You nearly hit your target, try better today!', icon="⚠️")
  
if yesterdays_metrics[0] <=95:
  rain(emoji="🚨",font_size=54,falling_speed=5,animation_length="5")
  st.error('Yesterday you were off track, try extra hard today!', icon='🚨')
  



options = st.multiselect('What do you want to visualise?', ['Overall', 'Health', 'Productivity', 'Personal', 'Goal Score'], default =['Goal Score', 'Overall'])

st.line_chart(data=df[options])

st.write('### 3 Day Averages')

option = {
  'series': [
    {
      'type': 'gauge',
      'color': '#ff4bd0',
      'progress': {
        'show': True,
        'width': 10,
        
      },
      'axisLine': {
        'lineStyle': {
          'width': 10
        }
      },
      'axisTick': {
        'show': False
      },
      'splitLine': {
        'length': 0,
        'lineStyle': {
          'width': 2,
          'color': '#ff4bd0'
        }
      },
      'axisLabel': {
        'distance': 10,
        'color': 'black',
        'fontSize': 20
      },
      'anchor': {
        'show': False,
        'color': '#ff4bd0',
        'showAbove': True,
        'size': 0,
        'itemStyle': {
          'borderWidth': 10,
          'color': '#ff4bd0'
        }
      },
      'title': {
       'show': False
      },
      'detail': {
        'valueAnimation': True,
        'fontSize': 60,
        'color': 'black',
        'offsetCenter':[0, '35%']
      },
      'data': [
        {
          'value': 70,
          
        }
      ]
    }
  ]
};

st_echarts(options=option)

st.write('### Week Averages')
st.write('calendar heatmap')