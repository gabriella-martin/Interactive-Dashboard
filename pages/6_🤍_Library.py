import streamlit as st
from instant_pipelines import welcome_pipeline
from streamlit_extras.app_logo import add_logo


add_logo("resources/logo_transparent_background.png", height=210)

st.write("""<style>@import url('https://fonts.googleapis.com/css2?family=Kanit');html, body, [class*="css"]  {  
   font-family: 'Kanit';  
}</style>""", unsafe_allow_html=True)


airtable=welcome_pipeline.AirTablePipeline()
currently_reading = airtable.get_currently_reading_books()
read_books = airtable.get_books_read_covers()


st.markdown("<h1 style='text-align: center;color: #FDF4DC;'>Read</h1>", unsafe_allow_html=True)
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






