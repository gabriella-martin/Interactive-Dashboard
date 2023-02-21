import requests
import datetime
import pandas as pd
import pickle
from decouple import config

df = pd.read_csv('Database.csv')
number_of_entries = len(df)


# get rid after first run

last_aggregate = ['00:00', '00:00']
pickle.dump(last_aggregate, open('last_aggregate', 'wb'))


class TrackingTimePipeline:

    def connect_to_api(self):

        url = 'https://app.trackingtime.co/api/v4/projects/times'
        response = requests.get(url, headers={'Content-Type': 'application/json', 'Authorization': config('TRACKING_TIME_API_KEY')})
        data = (response.json())['data']
        return data

    def get_aggregate_hours_spent_on_work_and_reading(self):
        data = self.connect_to_api()
        for type in data:
            if type['id'] == 1790207:
                reading_hours = type['loc_worked_hours']
                continue
        else:
            work_hours = type['loc_worked_hours']
        return(reading_hours, work_hours)

    def get_hours_done_today(self):
        todays_aggregates = self.get_aggregate_hours_spent_on_work_and_reading()
        last_aggregate = pickle.load(open("last_aggregate", "rb"))
        format = '%H:%M'
        reading_done_today = datetime.datetime.strptime(todays_aggregates[0], format) - datetime.datetime.strptime(last_aggregate[0], format)
        work_done_today = datetime.datetime.strptime(todays_aggregates[1], format) - datetime.datetime.strptime(last_aggregate[1], format)
        last_aggregate = [(str(datetime.datetime.strptime(todays_aggregates[0], format)))[11:-3],(str(datetime.datetime.strptime(todays_aggregates[1], format)))[11:-3]]
        pickle.dump(last_aggregate, open('last_aggregate', 'wb'))
        return(reading_done_today, work_done_today)


class ExistPipeline:

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


class WakaTimePipeline:

    def get_total_time_spent_coding_today(self):
        api_key = config('WAKATIME_API_KEY')
        url = f'https://wakatime.com/api/v1/users/gabriella01/summaries?api_key={api_key}&range=today'  
        response = requests.get(url)
        response = response.json()
        response = response['data'][0]['grand_total']
        time_in_decimal_format = response['decimal']
        return time_in_decimal_format




trackingtime = TrackingTimePipeline()
todays_hours_recorded = trackingtime.get_hours_done_today()
    
work_daily_hours = []

work_daily_hours.append(todays_hours_recorded[0])
work_daily_hours.append(todays_hours_recorded[1])
        
work_daily_hours_columns = ['Reading Hours', 'Work Hours']

git_hub_stats = []
exist = ExistPipeline()
todays_git_stats = exist.get_todays_streak()

git_hub_stats.append(todays_git_stats[0])
git_hub_stats.append(todays_git_stats[1])

git_hub_status_columns = ['GitHub Contributions', 'GitHub Streak']

coding_time = []
wakatime = WakaTimePipeline()
coding_time_today = wakatime.get_total_time_spent_coding_today()

coding_time.append(wakatime)


productivity_list = work_daily_hours + git_hub_stats + coding_time