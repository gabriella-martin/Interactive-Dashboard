import base64
import datetime
import requests
import streamlit as st

from decouple import config
from todoist_api_python.api import TodoistAPI

class TodoistPipeline:

    def __init__(self):
        api = TodoistAPI(st.secrets['TODOIST_API_KEY'])
        self.tasks = api.get_tasks()

    def get_todays_tasks(self):
        project_id= '2307182740'
        tasks_today = []
        for task in self.tasks:
            task = ((str(task))[4:]).split(', ')
            task[8] = task[8][14:-1]
            task[8] = datetime.datetime.strptime(task[8], '%Y-%m-%d')
            if project_id in task[-4]:
                task_name = (task[4])[9:-1]
                tasks_today.append(task_name)
        return tasks_today
    

class AirTablePipeline:

    def get_currently_reading_books(self):
        token = st.secrets['AIRTABLE_TOKEN_API']
        headers = {'Authorization': f"Bearer {token}"}

        response = requests.get('https://api.airtable.com/v0/appgTS4jpfHcqPeXA/tblSXX2los7etnqI0', headers=headers)

        response = response.json()
        response = response['records']

        currently_reading_covers = []
        currently_reading_percentages = []

        for item in response:
            if int(item['fields']['% Complete']) != 100:
                book_cover = item['fields']['Cover']
                currently_reading_covers.append(book_cover)
                percent_complete = item['fields']['% Complete']
                currently_reading_percentages.append(percent_complete)
                
        return currently_reading_covers, currently_reading_percentages
    def get_just_read_books(self):
        token = st.secrets['AIRTABLE_TOKEN_API']
        headers = {'Authorization': f"Bearer {token}"}

        response = requests.get('https://api.airtable.com/v0/appgTS4jpfHcqPeXA/tblSXX2los7etnqI0', headers=headers)

        response = response.json()
        response = response['records']

        just_read_covers = []
        for item in response:

            if str(item['fields']['Date Started']) == '2023-02-03':
                book_cover = item['fields']['Cover']
                just_read_covers.append(book_cover)
                

        return just_read_covers
    def get_books_read_covers(self):
        token = st.secrets['AIRTABLE_TOKEN_API']
        headers = {'Authorization': f"Bearer {token}"}

        response = requests.get('https://api.airtable.com/v0/appgTS4jpfHcqPeXA/tblSXX2los7etnqI0', headers=headers)

        response = response.json()
        response = response['records']

        read_covers = []

        for item in response:
            if int(item['fields']['% Complete']) == 100:
                book_cover = item['fields']['Cover']
                read_covers.append(book_cover)
                
        return read_covers

a = AirTablePipeline()
a.get_just_read_books()
class SpotifyPipeline:

    def __init__(self):
        self.spotify_id = st.secrets['SPOTIFY_CLIENT_ID']
        self.spotify_secret = st.secrets['SPOTIFY_CLIENT_SECRET'] 
        self.refresh_token = st.secrets['SPOTIFY_REFRESH_TOKEN']
    

    def get_new_token(self): 
        encoded = base64.b64encode((self.spotify_id + ":" + self.spotify_secret).encode("ascii")).decode("ascii")
        url = f'https://accounts.spotify.com/api/token?grant_type=refresh_token&refresh_token={self.refresh_token}'
        headers = {f"Content-Type" : "application/x-www-form-urlencoded", "Authorization": "Basic " + encoded }
        response = requests.post(url, headers=headers)
        response= response.json()
        access_token = response['access_token']
        return access_token

    def get_top_tracks(self):
        access_token = self.get_new_token()
        
        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"}

        response = requests.get('https://api.spotify.com/v1/me/top/tracks?limit=3&time_range=short_term', headers=headers)
        
        items = ((response.json())['items'])
        top_songs = [[], [], []]
        for index, item in enumerate(items):
            top_songs[index].append(item['name'])
            top_songs[index].append(item['artists'][0]['name'])
            top_songs[index].append(item['album']['images'][0]['url'])

        return top_songs
        
    def get_currently_playing(self):
        access_token = self.get_new_token()

        headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"}
        response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)
        
        if str(response) == '<Response [200]>':
            response = response.json()
            artist = response['item']['album']['artists'][0]['name']
            song_name = response['item']['name']
            image = response['item']['album']['images'][0]['url']
        
        else:
            headers = {'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"}
            response = requests.get('https://api.spotify.com/v1/me/player/recently-played?limit=1', headers=headers) 
            response=response.json()         
            artist = response['items'][0]['track']['album']['artists'][0]['name']
            song_name = response['items'][0]['track']['name']
            image = response['items'][0]['track']['album']['images'][0]['url']
        return artist, song_name, image

       

