import streamlit as st
from streamlit_extras.app_logo import add_logo
add_logo("logo_white_background.jpg", height=150)

import importlib 
DataPipeline = importlib.import_module('Data-Pipeline')

a=DataPipeline.AirTablePipeline()
currently_reading = a.get_currently_reading_books()
read_books = a.get_books_read_covers()

from streamlit_toggle import st_toggle_switch


toggle = st_toggle_switch(
    label="Currently Reading?",
    default_value=True,
    label_after=False,
    inactive_color="#D3D3D3",  # optional
    active_color="#11567f",  # optional
    track_color="#29B5E8")  # optional

if toggle == True:

    for cover in currently_reading:
        col1,col2 = st.columns([3,15])
        col1.image(image=cover, use_column_width='always')

if toggle == False:
    st.write('__All Read__')
    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(0, len(read_books), 5):

        col1.image(image=read_books[i],use_column_width='always')
    
    for  i in range(1, len(read_books), 5):

        col2.image(image=read_books[i], use_column_width='always')

    for  i in range(2, len(read_books), 5):

        col3.image(image=read_books[i], use_column_width='always')

    for  i in range(3, len(read_books), 5):

        col4.image(image=read_books[i], use_column_width='always')

    for  i in range(4, len(read_books), 5):

        col5.image(image=read_books[i], use_column_width='always')






