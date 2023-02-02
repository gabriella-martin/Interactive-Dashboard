import importlib 
import streamlit as st


from streamlit_extras.app_logo import add_logo


add_logo("logo_white_background.jpg", height=150)

DataPipeline = importlib.import_module('Data-Pipeline')
airtable=DataPipeline.AirTablePipeline()
currently_reading = airtable.get_currently_reading_books()
read_books = airtable.get_books_read_covers()


st.markdown("<h1 style='text-align: center;color: black;'>Books Read</h1>", unsafe_allow_html=True)
st.write('')
st.write('')


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






