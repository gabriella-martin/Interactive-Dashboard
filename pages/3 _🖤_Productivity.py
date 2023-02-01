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
st.write('')


# yesterday


import streamlit_nested_layout









metric_list = ['Productivity', 'Work Score', 'Reading Score']

import importlib 
DataPipeline = importlib.import_module('Data-Pipeline')

a=DataPipeline.AirTablePipeline()
currently_reading = a.get_currently_reading_books()



import important_metrics as im
productivity_metrics = im.ImportantMetrics(metric_list = ['Productivity', 'Work Score', 'Reading Score', 'GitHub Contributions', 'Coding Time'])
yesterdays_metrics = productivity_metrics.get_time_period_metric(1)
yesterday_vs_day_before_yesterday_percent_change = productivity_metrics.get_time_period_percent_change(1)
three_day_averages = productivity_metrics.get_time_period_metric(3)
current_three_day_vs_past_three_day = productivity_metrics.get_time_period_percent_change(1)
seven_day_averages = productivity_metrics.get_time_period_metric(7)
current_seven_day_vs_past_seven_day = productivity_metrics.get_time_period_percent_change(7)

# move to exist pipeline backend 
b = im.ImportantMetrics(metric_list)






yesterdays_streak = df.iloc[number_of_entries -1]['GitHub Streak']




one_day_commits_per_hour = productivity_metrics.commits_per_hour(1)
three_day_commits_per_hour = productivity_metrics.commits_per_hour(3)
seven_day_commits_per_hour = productivity_metrics.commits_per_hour(7)


date_range = st.select_slider(label = 'What date range would you like to see?', options = ['Yesterday', '3 Days', '7 Days'], label_visibility = 'collapsed', key=1)
outer_cols = st.columns([7,0.5,3.5])

 
with outer_cols[0]:
    
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
    with st.expander('**Daily Goals**', expanded=False):
        st.write('') 


    with st.expander('📖 **Currently Reading**', expanded=False):
    
        col1,col2,col3= st.columns(3)

        with col1:
        
            st.image(image=currently_reading[0][0], use_column_width='always')
            st.write(currently_reading[1][0] + '%')


        with col2 :
        
            st.image(image=currently_reading[0][1], use_column_width='always')
            st.write(currently_reading[1][1] + '%')
        with col3:
        
            st.image(image=currently_reading[0][2], use_column_width='always')
            st.write(currently_reading[1][2] + '%')
           




#moved to metrics


def get_time_coding_per_time_working():
    time_working = df.iloc[number_of_entries -1]['Work Hours']
    time_coding = df.iloc[number_of_entries -1]['Coding Time Decimal']
    percent_of_day_coding = round((float(time_coding) / float(time_working))*100)
    
    return percent_of_day_coding


def percent_of_three_day_coding():
    time_working_past_three_days = df.iloc[number_of_entries -1]['Work Hours'] + df.iloc[number_of_entries -2]['Work Hours'] + df.iloc[number_of_entries -3]['Work Hours']
    time_coding_past_three_days = df.iloc[number_of_entries -1]['Coding Time Decimal'] + df.iloc[number_of_entries -2]['Coding Time Decimal'] + df.iloc[number_of_entries -3]['Coding Time Decimal']
    percent_of_three_day_coding = round((float(time_coding_past_three_days) / float(time_working_past_three_days))*100)

    return percent_of_three_day_coding

def percent_of_seven_day_coding():
    time_working_past_seven_days = df.iloc[number_of_entries -1]['Work Hours'] + df.iloc[number_of_entries -2]['Work Hours'] + df.iloc[number_of_entries -3]['Work Hours'] + df.iloc[number_of_entries-4]['Work Hours'] +  + df.iloc[number_of_entries-5]['Work Hours']  + df.iloc[number_of_entries-6]['Work Hours']  + df.iloc[number_of_entries-7]['Work Hours']
    time_coding_past_seven_days = df.iloc[number_of_entries -1]['Coding Time Decimal'] + df.iloc[number_of_entries -2]['Coding Time Decimal'] + df.iloc[number_of_entries -3]['Coding Time Decimal']+ df.iloc[number_of_entries-4]['Coding Time Decimal'] +   df.iloc[number_of_entries-5]['Coding Time Decimal']  + df.iloc[number_of_entries-6]['Coding Time Decimal']  + df.iloc[number_of_entries-7]['Coding Time Decimal']
    percent_of_seven_day_coding = round((float(time_coding_past_seven_days) / float(time_working_past_seven_days))*100)
    
    return percent_of_seven_day_coding


percent_of_day_coding = (productivity_metrics.get_work_reading_coding_split(1))[0]
percent_of_working_not_coding = (100-percent_of_day_coding)
percent_of_three_day_coding = (productivity_metrics.get_work_reading_coding_split(3))[0]
percent_of_working_not_coding_three = 100 - percent_of_three_day_coding
percent_of_seven_day_coding = (productivity_metrics.get_work_reading_coding_split(2))[0]
percent_of_working_not_coding_seven = 100 - percent_of_seven_day_coding

labels = ['Non Coding Work', 'Coding']
if date_range =='Yesterday':
    values = [percent_of_working_not_coding, percent_of_day_coding]

elif date_range == '3 Days':
    values = [percent_of_working_not_coding_three, percent_of_three_day_coding]

elif date_range == '7 Days':
    values = [percent_of_working_not_coding_seven, percent_of_seven_day_coding]



st.write('')
figure = px.pie(title='Work Hours Split',height = 395, values=values, labels=labels, width=250,  hole=0.7, color = labels, color_discrete_map={labels[0]:'#6F4E37', labels[1]: '#9c8268'})
outer_columns =st.columns(2)
with outer_columns[0]:

    with st.expander('**😺 GitHub Statistics**', expanded=False):
        col1, col2 = st.columns(2)
        col1.write('')
        col2.write('')
        if date_range == '3 Days':
            
            col1.metric(label="Commits", value=three_day_averages[3], delta=str(current_three_day_vs_past_three_day[3]) + '%')

        if date_range == '7 Days':
            
            col1.metric(label="Commits", value=seven_day_averages[3], delta=str(current_seven_day_vs_past_seven_day[3]) + '%')


        if date_range == 'Yesterday':
            
            col1.metric(label="Commits", value=yesterdays_metrics[3], delta=str(yesterday_vs_day_before_yesterday_percent_change[3]) + '%')

    
        col2.write('')
        col2.metric(label='Streak', value = yesterdays_streak)

with outer_columns[1]:
    
    expand =st.expander('**💻 Coding Statistics**', expanded=False)

    with expand:
        st.write('')
        col1,col2 = st.columns(2)
        col2.write('')

            # change to nice format for display digital clock
        if date_range == '3 Days':
            
            col1.metric(label="Hours", value=three_day_averages[4], delta=str(current_three_day_vs_past_three_day[4]) + '%')
            col2.metric(label='Mits/hr', value = three_day_commits_per_hour)
        if date_range == '7 Days':
            
            col1.metric(label="Hours", value=seven_day_averages[4], delta=str(current_seven_day_vs_past_seven_day[4]) + '%')
            col2.metric(label='Mits/hr', value = seven_day_commits_per_hour)

        if date_range == 'Yesterday':
            
            col1.metric(label="Hours Coded",value=yesterdays_metrics[4], delta=str(yesterday_vs_day_before_yesterday_percent_change[4]) + '%')
            col2.metric(label='Commits/hr', value = one_day_commits_per_hour, )




one_day_full_split = (productivity_metrics.get_work_reading_coding_split(1))[1]
three_day_full_split= (productivity_metrics.get_work_reading_coding_split(3))[1]
seven_day_full_split = (productivity_metrics.get_work_reading_coding_split(7))[1]

labels = ['Non Coding Work', 'Coding','Reading']
if date_range =='Yesterday':
    values = one_day_full_split

elif date_range == '3 Days':
    values = three_day_full_split

elif date_range == '7 Days':
    values = seven_day_full_split


fig = px.pie(height = 400,title='Productive Hours Split', values=values, labels=labels, width=250, hole=0.7, names=labels,color = labels, color_discrete_map={labels[0]:'#6F4E37', labels[1]: '#9c8268', labels[2]: '#5C4033'})


col1, col2 = st.columns(2)

with col1:
    chart_1 = st.plotly_chart(figure, use_container_width=True)

with col2:
    chart_2 = st.plotly_chart(fig, use_container_width=True)

style_metric_cards( border_left_color='#6F4E37', border_size_px =2, border_color='#ccbea3', border_radius_px=10)

from streamlit_pills import pills
selected = pills('What to visualise', ['Productivity', 'Work Score', 'Reading Score', 'Work Hours', 'Reading Hours', 'Coding Time', 'GitHub Contributions'], ['🏹', '👩🏽‍💻', '📖','👩🏽‍💻', '📖', '⌨️', '😺'], label_visibility='collapsed')



if selected == 'Productivity' or selected == 'Work Score' or selected == 'Reading Score':
    fig = px.line(df, x='Days', y =[selected, 'Goal Score'], color_discrete_sequence=[ "#6F4E37", "#9c8268"])
    fig.update(layout_yaxis_range = [50,130])
    st.plotly_chart(fig, use_container_width=True)

else:
    fig = px.line(df, x='Days', y =selected, color_discrete_sequence= ["#6F4E37"])
    st.plotly_chart(fig, use_container_width=True)  




 













