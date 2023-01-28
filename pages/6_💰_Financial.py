import streamlit as st
from streamlit_extras.app_logo import add_logo
add_logo("logo_transparent_background.png", height=150)

import streamlit_nested_layout


outer_cols = st.columns([1, 1])

with outer_cols[0]:
    st.markdown('## Column 1')
    st.selectbox('selectbox', [1,2,3], key='sel1')
    
    inner_cols = st.columns([1, 1])
    with inner_cols[0]:
        st.markdown('Nested Column 1')
        st.selectbox('selectbox', [1,2,3], key='sel2')
    with inner_cols[1]:
        st.markdown('Nested Column 2')
        st.selectbox('selectbox', [1,2,3], key='sel3')
    
    

with outer_cols[1]:
    st.markdown('## Column 2')
    with st.expander('Expander 1', expanded=True):
        st.markdown('Some Stuff Here')
        with st.expander('Nested Expander 1', expanded=True):
            st.markdown('Some More Stuff Here')
            
            inner_cols = st.columns([1, 1])
            with inner_cols[0]:
                st.markdown('Nested Column 1')
                st.selectbox('selectbox', [1,2,3], key='sel4')
            with inner_cols[1]:
                st.markdown('Nested Column 2')
                st.selectbox('selectbox', [1,2,3], key='sel5')
        with st.expander('Nested Expander 2'):
            st.markdown('Some More Stuff Here')