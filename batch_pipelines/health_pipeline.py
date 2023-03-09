import csv
import datetime
import time
import requests
from decouple import config
from pyicloud import PyiCloudService
from shutil import copyfileobj

class AppleHealthPipeline:

    def __init__(self):
        self.todays_date_only = str(datetime.datetime.today())[:10] 
        self.api = PyiCloudService(config('APPLE_ID'), config('APPLE_ID_PASSWORD'))
        self.order_of_column_names_in_csvfile = ['Active Energy kj', 'Basal Energy Burned kj', 'Carbs g', 'Dietary Energy kj'
        , 'Dietary Sugar g', 'Protein g', 'Saturated Fat g', 'Steps Count', 'Total Fat']

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
            
        todays_health_data_document = self.api.drive[f'HealthAutoExport-{self.todays_date_only}-{self.todays_date_only} Data.csv']

        return(todays_health_data_document)      

    def extract_csv_data_to_python_list(self):

        todays_health_data_document = self.connect_to_api()
        todays_apple_health_data_in_list = []
        with todays_health_data_document.open(stream=True) as response:
            with open(todays_health_data_document.name, 'wb') as file_out:
                copyfileobj(response.raw, file_out)
        with open(f'HealthAutoExport-{self.todays_date_only}-{self.todays_date_only} Data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == 'Date':
                    continue
                else:
                    for i in range(1,10):
                        todays_apple_health_data_in_list.append(row[i])

        return(todays_apple_health_data_in_list)

    def convert_from_kj_to_kcals(self):

        todays_apple_health_data_in_list = self.extract_csv_data_to_python_list()

        for index, value in enumerate(self.order_of_column_names_in_csvfile):
            if 'kj' in value:
                todays_apple_health_data_in_list[index] = round(float(todays_apple_health_data_in_list[index])/4.184)

        return todays_apple_health_data_in_list

class WithingsPipeline:

    def connect_to_api(self):
        client_id = config('WITHINGS_CLIENT_ID')
        client_secret = config('WITHINGS_CLIENT_SECRET')
        refresh_token = config('WITHINGS_REFRESH_TOKEN')
        data = {'action': 'requesttoken','grant_type': 'refresh_token','client_id': f'{client_id}','client_secret': f'{client_secret}','refresh_token': f'{refresh_token}',}

        response = requests.post('https://wbsapi.withings.net/v2/oauth2', data=data)
        new_access_token = (response.json())['body']['access_token']

        headers =  {"Authorization": f"Bearer {new_access_token}"}
        today = (datetime.datetime.today())
        today_unix = time.mktime(today.timetuple())
        today_start_of_day_unix = time.mktime(today.timetuple())
        data = {'action': 'getmeas','meastypes': '1,6', 'start_time': f'{today_start_of_day_unix}', 'end_time': f'{today_unix}' }
        response = requests.post('https://wbsapi.withings.net/measure', headers=headers, data=data)
        response = response.json()
        return response
        
    def parse_data(self):
        
        todays_withings_body_measurements = []
        response = self.connect_to_api()
        data_items = response['body']['measuregrps'][0]['measures']
        for data_item in data_items:
            data_value = str((data_item['value']))[:2] + '.' + str((data_item['value']))[2:4]
            data_value = float(data_value)
            todays_withings_body_measurements.append(data_value)

        return(todays_withings_body_measurements)
        
class ExistPipeline:
        
        def get_sleep_data(self):
            todays_date = (str(datetime.datetime.today()))[:10]
            response = requests.get("https://exist.io/api/2/attributes/with-values",headers = {'Authorization': f"Token {config('EXIST_API_TOKEN')}"} )
            response =response.json()
            responses =  response['results'][4]['values']
            for response in responses:
    
                if response['date'] == todays_date:
                    sleep_time = response['value'] 

            sleep_hours = (str(sleep_time/60))

            return(sleep_hours)


if __name__ == '__main__':
    exist = ExistPipeline()
    sleep_hours = exist.get_sleep_data()
    todays_apple_health_data_in_list = (AppleHealthPipeline()).convert_from_kj_to_kcals()
    todays_withings_body_measurements=(WithingsPipeline()).parse_data()
    todays_full_health_data = todays_apple_health_data_in_list + todays_withings_body_measurements
    todays_full_health_data.append(sleep_hours)
    order_of_list_quantity_measure = ['Active Cals', 'Total Cals Burned', 'Carbs', 'Total Cals Consumed'
            , 'Sugar', 'Protein', 'Sat Fat', 'Steps', 'Fat', 'Body Weight kg', 'Body Fat %', 'Sleep Hours']




