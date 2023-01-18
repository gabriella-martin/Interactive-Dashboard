import csv
import datetime
import pickle
import requests
import shutil

from datetime import datetime, timedelta
from decouple import config
from pyicloud import PyiCloudService
from shutil import copyfileobj

class HealthPipeline:

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

class WorkPipeline:

    def __init__(self):

        self.url = 'https://app.trackingtime.co/api/v4/projects/times'
        self.response = requests.get(self.url, headers={'Content-Type': 'application/json', 'Authorization': config('TRACKING_TIME_API_KEY')})
        self.retrieve_data = (self.response.json())['data']
        self.work_daily_hours = []
        self.yesterdays_hours = ['00:00', '00:00']
        pickle.dump(self.yesterdays_hours, open('yesterday_hours', 'wb'))

class PersonalPipeline:
