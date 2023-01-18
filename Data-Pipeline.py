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

        
class WorkPipeline:

class PersonalPipeline:
