import streamlit as st

from streamlit_extras.app_logo import add_logo
add_logo("missmartin.jpeg", height=150)

import plotly.express as px
import pandas as pd

df = pd.read_csv('Database.csv')

select = st.multiselect(label = 'What scores do you want to visualise?', 
options=['Health', 'Steps Score', 'Active Cals Score', 'Diet', 'Goal Score'], default = ['Health', 'Goal Score'])

fig = px.line(df, x='Days', y=select, color_discrete_sequence=[ "pink", "hotpink", "deeppink",  'plum', 'darkmagenta'])
fig.update(layout_yaxis_range = [50,140])

st.plotly_chart(fig)


select_raw = st.selectbox(label = 'What raw data do you want to visualise?', 
options=[ 'Steps', 'Active Cals'])

if select_raw == 'Steps':
    figure = px.line(df, x='Days', y=['Steps', 'Steps Goal'], color_discrete_sequence=[ "pink", "hotpink",])
    figure.update(layout_yaxis_range = [4000,18000])
    st.plotly_chart(figure)


if select_raw == 'Active Cals':
    figure = px.line(df, x='Days', y=['Active Cals', 'Active Cals Goal'], color_discrete_sequence=[ "pink", "hotpink",])
    figure.update(layout_yaxis_range = [250,800])
    st.plotly_chart(figure)
