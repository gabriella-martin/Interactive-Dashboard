import important_metrics as im
import importlib 
import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit_nested_layout

from streamlit_extras.app_logo import add_logo
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_pills import pills


# styling

st.write("""<style>@import url('https://fonts.googleapis.com/css2?family=Kanit');html, body, [class*="css"]  {  
   font-family: 'Kanit';  
}</style>""", unsafe_allow_html=True)

color = '#6e6056'

style_metric_cards( background_color = color,border_left_color=color, border_size_px =0.3, border_color=color, border_radius_px=10)
add_logo("logo_transparent_background.png", height=210)


# loading data and important metrics


df = pd.read_csv('Database.csv')
number_of_entries = len(df)

DataPipeline = importlib.import_module('Data-Pipeline')
books=DataPipeline.AirTablePipeline()
currently_reading = books.get_currently_reading_books()

productivity_metrics = im.ImportantMetrics(metric_list = ['Work Hours', 'Reading Hours','Coding Hours',  'GitHub Contributions', 'Coding Hours'])
yesterdays_metrics = productivity_metrics.get_time_period_metric(1)
yesterday_vs_day_before_yesterday_percent_change = productivity_metrics.get_time_period_percent_change(1)
three_day_averages = productivity_metrics.get_time_period_metric(3)
current_three_day_vs_past_three_day = productivity_metrics.get_time_period_percent_change(1)
seven_day_averages = productivity_metrics.get_time_period_metric(7)
current_seven_day_vs_past_seven_day = productivity_metrics.get_time_period_percent_change(7)

one_day_commits_per_hour = productivity_metrics.commits_per_hour(1)
three_day_commits_per_hour = productivity_metrics.commits_per_hour(3)
seven_day_commits_per_hour = productivity_metrics.commits_per_hour(7)
percent_of_day_coding = (productivity_metrics.get_work_reading_coding_split(1))[0]
percent_of_working_not_coding = (100-percent_of_day_coding)
percent_of_three_day_coding = (productivity_metrics.get_work_reading_coding_split(3))[0]
percent_of_working_not_coding_three = 100 - percent_of_three_day_coding
percent_of_seven_day_coding = (productivity_metrics.get_work_reading_coding_split(2))[0]
percent_of_working_not_coding_seven = 100 - percent_of_seven_day_coding

one_day_full_split = (productivity_metrics.get_work_reading_coding_split(1))[1]
three_day_full_split= (productivity_metrics.get_work_reading_coding_split(3))[1]
seven_day_full_split = (productivity_metrics.get_work_reading_coding_split(7))[1]

yesterdays_streak = df.iloc[number_of_entries -1]['GitHub Streak']


# start of visual
with st.sidebar:
    st.markdown("<h4 style='text-align: center;color: #FDF4DC;'>Date Range Slider</t>", unsafe_allow_html=True)
    date_range = st.select_slider(label = 'DATE RANGE SLIDER', options = ['Yesterday', '3 Day Average', '7 Day Average'], label_visibility = 'collapsed')


st.markdown("<h1 style='text-align: center;color: #FDF4DC;'>Productivity Hub</h1>", unsafe_allow_html=True)

st.write('')

st.write('')

# first row


outer_cols = st.columns([7,0.5,3.5])

with outer_cols[0]:
    
    if date_range == '3 Day Average':
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Work Hours", value=three_day_averages[0], delta=str(current_three_day_vs_past_three_day[0]) + '%')
        col2.metric(label="Reading Hours", value=three_day_averages[1], delta=str(current_three_day_vs_past_three_day[1]) + '%')
        col3.metric(label="Coding Hours", value=three_day_averages[2], delta=str(current_three_day_vs_past_three_day[2]) + '%')

    if date_range == '7 Day Average':
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Work Hours", value=seven_day_averages[0], delta=str(current_seven_day_vs_past_seven_day[0]) + '%')
        col2.metric(label="Reading Hours", value=seven_day_averages[1], delta=str(current_seven_day_vs_past_seven_day[1]) + '%')
        col3.metric(label="Coding Hours", value=seven_day_averages[2], delta=str(current_seven_day_vs_past_seven_day[2]) + '%')

    if date_range == 'Yesterday':
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Work Hours", value=yesterdays_metrics[0], delta=str(yesterday_vs_day_before_yesterday_percent_change[0]) + '%')
        col2.metric(label="Reading Hours", value=yesterdays_metrics[1], delta=str(yesterday_vs_day_before_yesterday_percent_change[1]) + '%')
        col3.metric(label="Coding Hours", value=yesterdays_metrics[2], delta=str(yesterday_vs_day_before_yesterday_percent_change[2]) + '%')
    
with outer_cols[2]:
    st.write('')
    with st.expander('**Daily Goals**', expanded=True):
        st.write('8 Hours Work' +'  \n' + '2 Hours Reading' )


  
st.write('')


# second row


outer_columns =st.columns(2)
with outer_columns[0]:

    with st.expander('**😺 GitHub Statistics**', expanded=True):
        col1, col2 = st.columns(2)
        col1.write('')
        col2.write('')
        if date_range == '3 Day Average':
            
            col1.metric(label="Commits", value=three_day_averages[3], delta=str(current_three_day_vs_past_three_day[3]) + '%')

        if date_range == '7 Day Average':
            
            col1.metric(label="Commits", value=seven_day_averages[3], delta=str(current_seven_day_vs_past_seven_day[3]) + '%')


        if date_range == 'Yesterday':
            
            col1.metric(label="Commits", value=yesterdays_metrics[3], delta=str(yesterday_vs_day_before_yesterday_percent_change[3]) + '%')

    
        col2.write('')
        col2.metric(label='Streak', value = yesterdays_streak)

with outer_columns[1]:
    
    with st.expander('**💻 Coding Statistics**', expanded=True):

        st.write('')
        col1,col2 = st.columns(2)
        col2.write('')

        if date_range == '3 Day Average':
            
            col1.metric(label="Hours", value=three_day_averages[4], delta=str(current_three_day_vs_past_three_day[4]) + '%')
            col2.metric(label='Mits/hr', value = three_day_commits_per_hour)
        if date_range == '7 Day Average':
            
            col1.metric(label="Hours", value=seven_day_averages[4], delta=str(current_seven_day_vs_past_seven_day[4]) + '%')
            col2.metric(label='Mits/hr', value = seven_day_commits_per_hour)

        if date_range == 'Yesterday':
            
            col1.metric(label="Hours Coded",value=yesterdays_metrics[4], delta=str(yesterday_vs_day_before_yesterday_percent_change[4]) + '%')
            col2.metric(label='Commits/hr', value = one_day_commits_per_hour, )


# pie charts


labels = ['Non Coding Work', 'Coding']

if date_range =='Yesterday':
    values = [percent_of_working_not_coding, percent_of_day_coding]

elif date_range == '3 Day Average':
    values = [percent_of_working_not_coding_three, percent_of_three_day_coding]

elif date_range == '7 Day Average':
    values = [percent_of_working_not_coding_seven, percent_of_seven_day_coding]

work_hour_split = px.pie(title='Work Hours Split',height = 365, values=values, labels=labels, width=250,  hole=0.7, color = labels, color_discrete_map={labels[0]:'#e5ddd3', labels[1]: '#6e6056'})

labels = ['Non Coding Work', 'Coding','Reading']

if date_range =='Yesterday':
    values = one_day_full_split

elif date_range == '3 Day Average':
    values = three_day_full_split

elif date_range == '7 Day Average':
    values = seven_day_full_split

productive_hour_split = px.pie(height = 400,title='Productive Hours Split', values=values, labels=labels, width=250, hole=0.7, names=labels,color = labels, color_discrete_map={labels[0]:'#e5ddd3', labels[1]: '#6e6056', labels[2]: '#a69a8f'})

col1, col2 = st.columns(2)

with col1:
    st.write('')
    chart_1 = st.plotly_chart(work_hour_split, use_container_width=True)

with col2:
    chart_2 = st.plotly_chart(productive_hour_split, use_container_width=True)



# line graph of long term data


selected = pills('What to visualise', ['Productivity', 'Work Score', 'Reading Score', 'Work Hours', 'Reading Hours', 'Coding Hours', 'GitHub Contributions'], ['🏹', '👩🏽‍💻', '📖','👩🏽‍💻', '📖', '⌨️', '😺'], label_visibility='collapsed')

if selected == 'Productivity' or selected == 'Work Score' or selected == 'Reading Score':
    fig = px.line(df, x='Days', y =[selected, 'Goal Score'], color_discrete_sequence=["#6e6056", "#e5ddd3"])
    fig.update(layout_yaxis_range = [50,130])
    st.plotly_chart(fig, use_container_width=True)

else:
    fig = px.line(df, x='Days', y =selected, color_discrete_sequence= ["#6e6056"])
    st.plotly_chart(fig, use_container_width=True)  


# behind the scenes

 
with st.expander('**Behind The Scenes**', expanded=False):
    st.write('Work In Progress')












