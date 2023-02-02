import datetime
import requests
from decouple import config
from todoist_api_python.api import TodoistAPI

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
        return(percentages_list)
        
    def personal_pipeline(self):
        self.get_daily_task_count()
        self.get_weekly_task_count()
        self.get_daily_tasks_done()
        self.get_weekday_specific_tasks_done()
        collated_lists = self.collate_categories()
        self.find_percentages_of_completed(collated_lists)

class ExistPipeline:
    def get_mood_data(self):
        todays_date = (str(datetime.datetime.today()))[:10]
        response = requests.get("https://exist.io/api/2/attributes/with-values", 
                headers = {'Authorization': f"Token {config('EXIST_API_TOKEN')}"} )

        todays_date = (str(datetime.datetime.today()))[:10]
        response = (response.json())  
        for i in response:
            if response['results'][2]['values'][0]['date'] == todays_date:

                mood_today = response['results'][2]['values'][0]['value']
            
        return mood_today




todoist = TodoistAPI()
percentages_list = todoist.personal_pipeline()


exist = ExistPipeline()
mood_today = exist.get_mood_data()

percentages_list.append(mood_today)

percentage_list_columns = ['Cleaning', 'Dogs', 'Self-Care, 'Mood']