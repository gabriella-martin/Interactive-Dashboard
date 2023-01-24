import csv
import datetime
import pickle
import requests
import shutil

from datetime import  timedelta
from decouple import config
from pyicloud import PyiCloudService
from shutil import copyfileobj
from todoist_api_python.api import TodoistAPI
from withings_api import WithingsAuth, WithingsApi, AuthScope
from withings_api.common import get_measure_value, MeasureType
from urllib import parse

class AppleHealthPipeline:

    def __init__(self):
        self.yesterdays_date_only = (str(datetime.today() - timedelta(1)))[:10]
        self.api = PyiCloudService(config('APPLE_ID'), config('APPLE_ID_PASSWORD'))
        self.yesterdays_data_in_list = []

    def connect_to_api(self):
        if self.api.requires_2fa:
            print("Two-factor authentication required.")
            code = input("Enter the code you received of one of your approved devices: ")
            result = self.api.validate_2fa_code(code)
            print("Code validation result: %s" % result)

            if not result:
                print("Failed to verify security code")
                sys.exit(1)

            if not self.api.is_trusted_session:
                print("Session is not trusted. Requesting trust...")
                result = self.api.trust_session()
                print("Session trust result %s" % result)

                if not result:
                    print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
            
        self.yesterdays_health_data_document = self.api.drive[f'HealthAutoExport-{self.yesterdays_date_only}-{self.yesterdays_date_only} Data.csv']

        return(self.yesterdays_health_data_document)      

    def extract_csv_data_to_python_list(self):

        with self.yesterdays_health_data_document.open(stream=True) as response:
            with open(self.yesterdays_health_data_document.name, 'wb') as file_out:
                copyfileobj(response.raw, file_out)
        with open(f'HealthAutoExport-{self.yesterdays_date_only}-{self.yesterdays_date_only} Data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == 'Date':
                    continue
                else:
                    self.yesterdays_data_in_list.append(row[1])
                    self.yesterdays_data_in_list.append(row[2])
                    self.yesterdays_data_in_list.append(row[3])
                    self.yesterdays_data_in_list.append(row[5])
        return(self.yesterdays_data_in_list)

    def get_health_data(self):
        self.connect_to_api()
        self.extract_csv_data_to_python_list()

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
        yesterday = pickle.load(open("yesterday_hours", "rb"))
        format = '%H:%M'
        reading_done_today = datetime.strptime(todays_aggregates[0], format) - datetime.strptime(yesterday[0], format)
        work_done_today = datetime.strptime(todays_aggregates[1], format) - datetime.strptime(yesterday[1], format) 
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

#class WithingsPipeline:

def get_data():
    headers =  {"Authorization": f"Bearer {config('WITHINGS_ACCESS_TOKEN')}"}
    data = {
    'action': 'getmeas',
    'meastypes': '1,6,8,76' }
    
    response = requests.post('https://wbsapi.withings.net/measure', headers=headers, data=data)
    print(response.json())

get_data()    
 


