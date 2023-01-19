# streamlit run Streamlit.py

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards



df = pd.read_csv('Database.csv')
number_of_entries = len(df)
get_last_entry_productivity_score = round((df.iloc[number_of_entries -1])['Overall'])

st.write("### Yesterday's Metrics")

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Overall", value=round((df.iloc[number_of_entries -1])['Overall']), delta=1000)
col2.metric(label="Health", value=round((df.iloc[number_of_entries -1])['Health']), delta=-1000)
col3.metric(label="Productivity", value=round((df.iloc[number_of_entries -1])['Productivity']), delta=0)
col4.metric(label="Personal", value=round((df.iloc[number_of_entries -1])['Personal']), delta=0)
style_metric_cards( border_left_color='#E035E2')

