
import streamlit as st
from streamlit_extras.app_logo import add_logo




add_logo("logo_white_background.jpg", height=150)

st.write("""<style>@import url('https://fonts.googleapis.com/css2?family=Kanit');html, body, [class*="css"]  {  
   font-family: 'Kanit';  
}</style>""", unsafe_allow_html=True)