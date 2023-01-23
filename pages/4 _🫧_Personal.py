
import streamlit as st
from streamlit_extras.app_logo import add_logo
add_logo("missmartin.jpeg", height=150)
import plotly.express as px
import pandas as pd

df = pd.read_csv('Database.csv')



number_of_entries = len(df)
from streamlit_extras.metric_cards import style_metric_cards
style_metric_cards( border_left_color='#ff4bd0')



st.write('### Personal')
# yesterday
st.markdown("<h4 style='text-align: center;color: black;'>Short Term</h4>", unsafe_allow_html=True)

metric_list = ['Personal', 'Dogs', 'Cleaning', 'Self-Care']
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

# three day and seven day


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
