import requests
import streamlit as st


def get_just_read_books():
        token = st.secrets['AIRTABLE_TOKEN_API']
        headers = {'Authorization': f"Bearer {token}"}

        response = requests.get('https://api.airtable.com/v0/appgTS4jpfHcqPeXA/tblSXX2los7etnqI0', headers=headers)

        response = response.json()
        response = response['records']
        num_of_books = len(response)
        just_read_covers = []
        for item in response:
            if int(item['fields']['% Complete']) == 100:
                if item['fields']['Number'] == (num_of_books-3) or item['fields']['Number'] == (num_of_books-4) or item['fields']['Number'] == (num_of_books-5):
                    cover = (item['fields']['Cover'])
                    rating = item['fields']['Rating /5']
                    just_read_covers.append(cover)
                    just_read_covers.append(rating)

        return just_read_covers

get_just_read_books()