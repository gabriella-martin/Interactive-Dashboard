# streamlit run Streamlit.py

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.let_it_rain import rain
from datetime import datetime
import json

import plotly.graph_objects as go
from streamlit_echarts import st_echarts
from streamlit_extras.app_logo import add_logo

add_logo("missmartin.jpeg", height=150)

df = pd.read_csv('Database.csv')
number_of_entries = len(df)

st.write("### Yesterday's Metrics")
st.write('>randomised Quote about better than yesterday')

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
def create_gauges():
  gauges = []
  for index, metric in enumerate(three_day_averages):
    gauge={ 'grid': {'bottom':0}, 'title':{'text':metric_list[index], 'left':'center', 'top':50},  'series':[  { 'type':'gauge',  'color':'#ff4bd0',  'progress':{  'show':True,  'width':8,    },  'axisLine':{  'lineStyle':{  'width':10  }  },  
'axisTick':{  'show':False  },  'splitLine':{  'length':0,  'lineStyle':{  'width':2,  'color':'#ff4bd0'  }  },  'axisLabel':{  'distance':10,  'color':'black',  'fontSize':10  },  
'anchor':{  'show':False,  'color':'#ff4bd0',  'showAbove':True,  'size':0,  'itemStyle':{  'borderWidth':10,  'color':'#ff4bd0'  }  },  'title':{ 'text' : 'yee', 'show':True  },  
  'pointer': {'width':3, 'length' : '40%' },'detail':{  'valueAnimation':True,  'fontSize':15.5,  'color':'black',  'offsetCenter':[0,'35%']  },  'data':[  {  'value':metric,    }  ]  }  ]  }
    gauges.append(gauge)
  return gauges


gauges = create_gauges()

col1, col2, col3, col4 = st.columns(4)

with col1:
  st_echarts(options=gauges[0])
with col2:
  st_echarts(options=gauges[1])
with col3:
  st_echarts(options=gauges[2])
with col4:
  st_echarts(options=gauges[3])

st.write('### Week Averages')

def get_seven_day_average():
  seven_day_averages = []
  for category in metric_list:
    yesterday_metric = df.iloc[number_of_entries -1][category]
    yesterday_minusone_metric = df.iloc[number_of_entries -2][category]
    yesterday_minustwo_metric = df.iloc[number_of_entries -3][category]
    yesterday_minusthree_metric = df.iloc[number_of_entries -4][category]
    yesterday_minusfour_metric = df.iloc[number_of_entries -5][category]
    yesterday_minusfive_metric = df.iloc[number_of_entries -6][category]
    yesterday_minussix_metric = df.iloc[number_of_entries -7][category]
    seven_day_average =round((yesterday_metric + yesterday_minusone_metric + yesterday_minustwo_metric+ yesterday_minusthree_metric + yesterday_minusfour_metric 
    +yesterday_minusfive_metric+yesterday_minussix_metric)/6)
    seven_day_averages.append(seven_day_average)
  return seven_day_averages

seven_day_averages = get_seven_day_average()

def create_gauges():
  seven_day_gauges = []
  for index, metric in enumerate(seven_day_averages):
    gauge={ 'grid':{ 'left': 0,'top': 30,'right': 0,'bottom': 30},'title':{'text':metric_list[index], 'left':'center', 'top':50},  'series':[  {  'type':'gauge',  'color':'#ff4bd0',  'progress':{  'show':True,  'width':8,    },  'axisLine':{  'lineStyle':{  'width':10  }  },  
'axisTick':{  'show':False  },  'splitLine':{  'length':0,  'lineStyle':{  'width':2,  'color':'#ff4bd0'  }  },  'axisLabel':{  'distance':10,  'color':'black',  'fontSize':10  },  
'anchor':{  'show':False,  'color':'#ff4bd0',  'showAbove':True,  'size':0,  'itemStyle':{  'borderWidth':10,  'color':'#ff4bd0'  }  },  'title':{ 'text' : 'yee', 'show':True  },  
  'pointer': {'width':3, 'length' : '40%' },'detail':{  'valueAnimation':True,  'fontSize':15.5,  'color':'black',  'offsetCenter':[0,'35%']  },  'data':[  {  'value':metric,    }  ]  }  ]  }
    seven_day_gauges.append(gauge)
  return seven_day_gauges

seven_day_gauges = create_gauges()

col1, col2, col3, col4 = st.columns(4)

with col1:
  st_echarts(options=seven_day_gauges[0])
with col2:
  st_echarts(options=seven_day_gauges[1])
with col3:
  st_echarts(options=seven_day_gauges[2])
with col4:
  st_echarts(options=seven_day_gauges[3])
st.write('### Overall Score Heatmap')

z = df['Overall']
x = df['Month']
y = df['Day of Month']
heatmap = go.Figure([go.Heatmap(z=z, x=x, y=y, colorscale=[[0, 'rgb(222, 195, 210)'],[1, 'rgb(196, 6, 147)']])])
heatmap.update_layout( xaxis_title = 'Month', yaxis_title = 'Day of Month')
heatmap.update_xaxes(title_font_color='black')
heatmap.update_yaxes(title_font_color='black')

st.plotly_chart(heatmap)

st.write('color numbers')