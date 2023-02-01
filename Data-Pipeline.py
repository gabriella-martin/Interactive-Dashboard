import base64
import csv
import datetime
import os.path
import pickle
import requests
import shutil

from datetime import  timedelta
from decouple import config
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from todoist_api_python.api import TodoistAPI


class TrackingTimePipeline:

    def __init__(self):

        self.url = 'https://app.trackingtime.co/api/v4/projects/times'
        self.response = requests.get(self.url, headers={'Content-Type': 'application/json', 'Authorization': config('TRACKING_TIME_API_KEY')})
        self.retrieve_data = (self.response.json())['data']
        self.work_daily_hours = []
        self.yesterdays_hours = ['00:00', '00:00']
        pickle.dump(self.yesterdays_hours, open('yesterday_hours', 'wb'))

    def get_aggregate_hours_spent_on_work_and_reading(self):
        for type in self.retrieve_data:
            if type['id'] == 1790207:
                reading_hours = type['loc_worked_hours']
                continue
        else:
            work_hours = type['loc_worked_hours']
        return(reading_hours, work_hours)

    def get_hours_done_today(self, todays_aggregates):
        end_of_day_today = pickle.load(open("yesterday_hours", "rb"))
        format = '%H:%M'
        reading_done_today = datetime.strptime(todays_aggregates[0], format) - datetime.strptime(end_of_day_today[0], format)
        work_done_today = datetime.strptime(todays_aggregates[1], format) - datetime.strptime(end_of_day_today[1], format) 
        pickle.dump(work_done_today, open('yesterday_hours', 'wb'))
        return(reading_done_today, work_done_today)

    def store_values_in_list(self, todays_hours_recorded):
        for value in todays_hours_recorded:
            self.work_daily_hours.append(str(value))
        return(self.work_daily_hours)

    def get_work_data(self):
        todays_aggregates = self.get_aggregate_hours_spent_on_work_and_reading()
        todays_hours_recorded = self.get_hours_done_today(todays_aggregates)
        self.store_values_in_list(todays_hours_recorded)

class TodoistPipeline:

    def __init__(self):
        api = TodoistAPI(config('TODOIST_API_KEY'))
        self.tasks = api.get_tasks()
        self.daily_section_id = ['109399215', '109857457', '109865778']
        self.weekly_section_id = {'0': 109913929, '1': 110024847, '2': 110024848, '3': 110024852, '4': 110024855, '5': 110024934, '6': 110024936}
        self.daily_completed_tasks = []
        self.section_number_of_tasks = []
        self.completed_percentages = []
        self.today = (datetime.datetime.today())
        self.today = self.today.replace(hour=23, minute=59, second=59, microsecond=999999)
        self.today_str = str((self.today))[:10]
        self.day_of_the_week = str(self.today.weekday())
        
        
    def get_daily_tasks_done(self):
        for id in self.daily_section_id:
            total_completed_tasks = 0
            for task in self.tasks:
                task = ((str(task))[4:]).split(', ')
                task[8] = task[8][14:-1]
                task[8] = datetime.datetime.strptime(task[8], '%Y-%m-%d')
                if id in task[-3] and task[8] > self.today:
                    total_completed_tasks +=1
            self.daily_completed_tasks.append(total_completed_tasks)
        return(self.daily_completed_tasks)   

    def get_daily_task_count(self):
        for id in self.daily_section_id:
            total_section_tasks = 0
            for task in self.tasks:
                task = ((str(task))[4:]).split(', ')
                if id in task[-3]:
                    total_section_tasks +=1
                
            self.section_number_of_tasks.append(total_section_tasks)
        return self.section_number_of_tasks

    def get_weekday_specific_tasks_done(self):
        todays_weekly_section = self.weekly_section_id[self.day_of_the_week]
        total_completed_tasks_cleaning = 0
        total_completed_tasks_dogs = 0
        total_completed_tasks_beauty = 0
        for task in self.tasks: 
            task = ((str(task))[4:]).split(', ')
            task[8] = task[8][14:-1]
            task[8] = datetime.datetime.strptime(task[8], '%Y-%m-%d')
            task[7] = (task[7][13:-1])
            if task[7] == '':
                if str(todays_weekly_section) in task[-3] and task[8] > self.today:
                    total_completed_tasks_cleaning +=1
            if task[7] == 'dogs':
                if str(todays_weekly_section) in task[-3] and task[8] > self.today:
                    total_completed_tasks_dogs +=1
            if task[7] == 'beauty':
                if str(todays_weekly_section) in task[-3] and task[8] > self.today:
                    total_completed_tasks_beauty +=1
        self.daily_completed_tasks.append(total_completed_tasks_cleaning)
        self.daily_completed_tasks.append(total_completed_tasks_dogs)
        self.daily_completed_tasks.append(total_completed_tasks_beauty)
        

        return(self.daily_completed_tasks)

    def get_weekly_task_count(self):
        total_section_tasks_cleaning = 0
        total_section_tasks_dogs = 0
        total_section_tasks_beauty = 0
        todays_weekly_section = self.weekly_section_id[self.day_of_the_week]
        for task in self.tasks:
            task = ((str(task))[4:]).split(', ')
            task[7] = (task[7][13:-1])
            if str(todays_weekly_section) in task[-3]:
                if task[7] == '':
                    total_section_tasks_cleaning +=1

                elif task[7] == 'dogs':
                    total_section_tasks_dogs +=1

                elif task[7] == 'beauty':
                        total_section_tasks_beauty +=1

        self.section_number_of_tasks.append(total_section_tasks_cleaning)
        self.section_number_of_tasks.append(total_section_tasks_dogs)
        self.section_number_of_tasks.append(total_section_tasks_beauty)
            
        return(self.section_number_of_tasks)
    
    def collate_categories(self):
        collated_list_completed = []
        collated_list_count = []

        for index, value in enumerate(self.daily_completed_tasks):
            if index <= 2:
                collated = value + (self.daily_completed_tasks)[index+3]
                collated_list_completed.append(collated)
            else: break
            

        for index, value in enumerate(self.section_number_of_tasks):
            if index <= 2:
                collated = value + (self.section_number_of_tasks)[index+3]
                collated_list_count.append(collated)
            else: break

        return(collated_list_completed, collated_list_count)


    def find_percentages_of_completed(self, collated_lists):


        find_fraction_complete = [b / m for b,m in zip(collated_lists[0], collated_lists[1])]
        percentages_list = []
        percentages_list = [str(round(item * 100)) + '%' for item in find_fraction_complete]
        print(percentages_list)
        
    def personal_pipeline(self):
        self.get_daily_task_count()
        self.get_weekly_task_count()
        self.get_daily_tasks_done()
        self.get_weekday_specific_tasks_done()
        collated_lists = self.collate_categories()
        self.find_percentages_of_completed(collated_lists)

import pandas as pd
import plotly.express as px

df = pd.read_csv('Database.csv')
number_of_entries = len(df)
class GoogleCalendarPipeline:

    def __init__(self):
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        self.service = build('calendar', 'v3', credentials=creds)
        self.now = datetime.datetime.utcnow().isoformat() + 'Z'
        self.time_now = datetime.datetime.today()
        self.start_of_day_today = self.time_now.replace(hour=00, minute=00, second=00)
        self.end_of_day_today = self.time_now.replace(hour=23, minute=59, second=59, microsecond=999999)
        self.start_of_day_today = (self.start_of_day_today).isoformat() + 'Z'
        self.end_of_day_today = (self.end_of_day_today).isoformat() + 'Z'
    
        
    def get_todays_events(self):
        events_result = self.service.events().list(calendarId='primary', timeMin=self.start_of_day_today, timeMax=self.end_of_day_today,
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        all_event_data = []
        for event in events:
            event_data = []
            event_name = (event['summary'])
            start_time = str(event['start']['dateTime'])[11:-4]
            end_time = str((event['end']['dateTime']))[11:-4]
            event_data.extend([event_name, start_time, end_time])
            all_event_data.append(event_data)

        return(all_event_data)

class ExistPipeline():

    def get_github_contributions(self):
        
        response = requests.get("https://exist.io/api/1/users/gabriellamartin/attributes/commits/", 
                headers = {'Authorization': f"Token {config('EXIST_API_TOKEN')}"} )
        todays_date = (str(datetime.datetime.today()))[:10]
        
        response = (response.json())  

        responses =  response['results']

        for response in responses:
            if response['date'] == todays_date:
                todays_commits = response['value'] 
                
        
        return todays_commits

    def get_todays_streak(self):
        todays_commits = self.get_github_contributions()
        yesterdays_streak = df.iloc[number_of_entries -1]['GitHub Streak']
        if todays_commits != 0:
            todays_streak = yesterdays_streak + 1
        else:
            todays_streak = 0 
        

        return todays_commits, todays_streak

# wrote to csv

    def get_mood_data(self):
        todays_date = (str(datetime.datetime.today()))[:10]
        response = requests.get("https://exist.io/api/2/attributes/with-values", 
                headers = {'Authorization': f"Token {config('EXIST_API_TOKEN')}"} )

        todays_date = (str(datetime.datetime.today()))[:10]
        response = (response.json())  

        if response['results'][2]['values'][0]['date'] == todays_date:

            mood_yesterday = response['results'][2]['values'][0]['value']
            
       
        if response['results'][3]['values'][0]['date'] == todays_date:

            journal_yesterday = response['results'][3]['values'][0]['value']
            
        return mood_yesterday, journal_yesterday

    def get_sleep_data(self):
        todays_date = (str(datetime.datetime.today()))[:10]
        response = requests.get("https://exist.io/api/2/attributes/with-values",headers = {'Authorization': f"Token {config('EXIST_API_TOKEN')}"} )
        todays_date = (str(datetime.datetime.today()))[:10]
        response = (response.json())

        responses =  response['results'][7]['values']
        for response in responses:
            
            if response['date'] == todays_date:
                wake_time = response['value'] 
            #in minutes from midnight

        wake_hour = (str(wake_time/60))[:1]
        wake_minutes = round(((int((str(wake_time/60))[2:4]))/100)*60)
        wake_string = wake_hour + ':' + str(wake_minutes) + 'am'
        
        response = requests.get("https://exist.io/api/2/attributes/with-values",headers = {'Authorization': f"Token {config('EXIST_API_TOKEN')}"} )
        response =response.json()
        responses =  response['results'][4]['values']
        for response in responses:
            if response['date'] == todays_date:
        
                sleep_time = response['value'] 
        

        sleep_hours = (str(sleep_time/60))[:1]
        sleep_minutes = round(((int((str(sleep_time/60))[2:4]))/100)*60)
        sleep_string = sleep_hours + 'hr' + str(sleep_minutes)
    
        return(sleep_string, wake_string, sleep_time)


class AirTablePipeline():

    def get_currently_reading_books(self):
        token = config('TOKEN_API')
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

'''    def get_books_read_covers(self):
        token = config('TOKEN_API')
        headers = {'Authorization': f"Bearer {token}"}

        response = requests.get('https://api.airtable.com/v0/appgTS4jpfHcqPeXA/tblSXX2los7etnqI0', headers=headers)

        response = response.json()
        response = response['records']

        read_covers = []

        for item in response:
            if item['fields']['Reading?'] == 'no':
                book_cover = item['fields']['cover']
                read_covers.append(book_cover)
                
        return read_covers
'''


class WakaTimePipeline:

    def get_total_time_spent_coding_today(self):
        api_key = config('WAKATIME_API_KEY')
        url = f'https://wakatime.com/api/v1/users/gabriella01/summaries?api_key={api_key}&range=today'  
        response = requests.get(url)
        response = response.json()
        response = response['data'][0]['grand_total']
        time_in_decimal_format = response['decimal']
        return time_in_decimal_format


class SpotifyPipeline:

    def __init__(self):
        self.spotify_id = config('SPOTIFY_CLIENT_ID')    
        self.spotify_secret = config('SPOTIFY_CLIENT_SECRET') 
        self.refresh_token = config('SPOTIFY_REFRESH_TOKEN')
    

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
        
        headers = {
            'Content-Type': 'application/json',"Authorization": f"Bearer {access_token}"
        }

        response = requests.get('https://api.spotify.com/v1/me/top/tracks?limit=3&time_range=short_term', headers=headers)
        
        items = ((response.json())['items'])
        top_songs = [[], [], []]
        for index, item in enumerate(items):
            top_songs[index].append(item['name'])
            top_songs[index].append(item['artists'][0]['name'])
            top_songs[index].append(item['album']['images'][0]['url'])

        return top_songs
            