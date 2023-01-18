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

        
class WorkPipeline:

class PersonalPipeline:
