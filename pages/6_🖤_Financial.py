import streamlit as st
from streamlit_extras.app_logo import add_logo
add_logo("logo_white_background.jpg", height=150)

import streamlit_nested_layout
import requests
url ='https://assets7.lottiefiles.com/private_files/lf30_y9czxcb9.json'
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_json = load_lottieurl(url)
st_lottie(lottie_json)

with st.expander('**Brainstorming Ideas**', expanded=False):
    st.write('monzo api, quant')