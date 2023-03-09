
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Financial",
    page_icon="resources/logo_transparent_background.png",
    layout="wide",
    initial_sidebar_state='auto')
add_logo("resources/logo_transparent_background.png", height=210)

st.write("""<style>@import url('https://fonts.googleapis.com/css2?family=Kanit');html, body, [class*="css"]  {  
   font-family: 'Kanit';  
}</style>""", unsafe_allow_html=True)

url ='https://assets7.lottiefiles.com/private_files/lf30_y9czxcb9.json'


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_json = load_lottieurl(url)
st_lottie(lottie_json)
with st.expander('**Brainstorming Ideas**', expanded=False):
    st.write('**Monzo Personal API**: Monzo provide a personal API [here](https://docs.monzo.com/#introduction), this will be behind streamlit personal authentication so only I can access the data. Involves moving my banking over to Monzo, something I want to do anyway')
