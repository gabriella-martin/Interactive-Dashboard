<h2 align="center">Interactive Dashboard</h2>

<h4 align="center">Languages and Technologies</h4>

<div align="center">
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" height="40" width="52"   />
	 <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="40" width="52"  />
	<img src="https://toppng.com/uploads/preview/rest-api-icon-rest-api-icon-11553510526uqs2ynyga2.png" alt="html5" width="40" height="40"/>
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apple/apple-original.svg"  width="40" height="40"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="40" width="52"   />
    <img src="https://avatars.githubusercontent.com/u/45109972?s=280&v=4" height="40" width="52"   />
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Matplotlib_icon.svg/2048px-Matplotlib_icon.svg.png" height="40" width="52"   /> </div>

<h2 align="center">Introduction</h2>
As someone who loves collecting data on my daily life, I was motivated by the need to simplify the often cumbersome process of accessing and analyzing data that plays a crucial role in my daily life. Before creating this dashboard, I found myself frequently jumping between multiple apps and sources of information just to gather the data I needed to make informed decisions about my health, work, and other important aspects of my life.

Not only was this approach inefficient and time-consuming, but it also made it difficult to get a complete and holistic view of the data I was dealing with. It was a challenge to track trends over time, identify patterns, and draw meaningful insights from the information at my disposal. In short, the lack of a centralized, user-friendly platform for managing my personal data was hindering my ability to live a more organized, productive, and fulfilling life.

That's where this app comes in. By consolidating all of my personal data in one place and presenting it in a visually appealing and intuitive manner, this dashboard has made it much easier for me to monitor my progress, identify areas for improvement, and stay on top of the things that matter most to me; this app has become an indispensable tool for helping me stay organized, focused, and in control of my life.

I began by making a list of metrics I wanted to track in four core categories; general, health, personal and productivity. I dedicated a page to each of these categories in my dashboard

To view the dashboard (with dummy data for privacy), go to this [link](https://gabriella-martin-interactive-dashboard-welcome-9hpibj.streamlit.app/)

**Dashboarding Software**

Streamlit is a Python library that I chose to use for building my dashboard because of its simplicity, flexibility, and ease of use. I also chose to use Streamlit because I wanted to focus on improving my backend development skills while still being able to create a polished and user-friendly frontend for my dashboard. Streamlit provided an ideal solution to this challenge by enabling me to quickly build a professional-looking dashboard without requiring extensive knowledge of front-end development. This allowed me to focus more on the data processing and analysis that is critical to my project while still delivering a polished and responsive user experience. If you are a Python user, check it out [here]( https://docs.streamlit.io/)!


<h2 align="center">Welcome Data</h2>

*The full code for my welcome page pipeline can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/tree/main/RealTime_Pipelines), the code for the frontend can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/Welcome.py)*


*All code on the home page is pulled once the page is loaded to ensure it is in accurate in real-time*

The homepage of my dashboard provides a snapshot of key information that I need to track on a daily basis. It includes the weather, upcoming football games, my to-do list, current tube status, and recently listened to music. The purpose of the homepage is to give me a quick and easy overview of the most important information I need to know at a glance. This enables me to plan my day efficiently and stay on top of my tasks and goals. 

**NASA Image of the Day**

NASA has multiple [API's](https://api.nasa.gov/), my favourite being the image of the day. As the name suggests, the API returns a mesmorizing space related picture each day. Here us one of my favourites

 ![NasaIOD](https://apod.nasa.gov/apod/image/2301/crtastro_0172_1097p.jpg)

Their REST-API is incredibly easy to use

```python
def nasa_image_of_the_day():

    url = 'https://api.nasa.gov/planetary/apod?api_key={apikey}'
    response = requests.get(url)
    nasa_image = (response.json())['hdurl']
    title_of_image = (response.json()['title'])
    return nasa_image, title_of_image
	
```
**Recent Music**

As part of my dashboard's welcome page, I have integrated Spotify's [API](https://developer.spotify.com/documentation/web-api/) to provide information on my music listening habits. The API seamlessly integrates with the welcome page, displaying the track that I am currently listening to. If I am not listening to anything at the moment, the API instead pulls information on the most recently played track. The ability to grab album artwork adds a visually appealing touch to the dashboard.

Spotify uses OAuth 2.0 and the steps to get the tokens needed are in the docs. The code for pulling currently listening to or just listened to is as follows:

```python
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
```

**Current Weather**

I added a weather section to the welcome page of my dashboard to provide quick and easy access to the current weather conditions. This feature helps me to plan my day accordingly by giving me an idea of what to expect weather-wise. I retrieve the current temperature, current condition (which I format into an emoji), sunrise and sunset. There are many options for a free weather API but I use this [one](https://www.weatherapi.com/).

```python
def get_weather():
  key = st.secrets['WEATHER_API_KEY']
  url = f'https://api.openweathermap.org/data/3.0/onecall?lat=51.46&lon=0.01&exclude=minutely,hourly,daily,alerts&appid={key}&units=metric'
  response = (requests.get(url)).json()
  json_response = response

  sunrise_time_epoch = json_response['current']['sunrise']
  sunset_time_epoch = json_response['current']['sunset']
  temperature = round(json_response['current']['temp'])
  condition = (json_response['current']['weather'][0]['description']).title()
  sunrise_time = datetime.fromtimestamp(sunrise_time_epoch).strftime('%H:%M')
  sunset_time = datetime.fromtimestamp(sunset_time_epoch).strftime('%I:%M')

  return(sunrise_time, sunset_time, temperature, condition)

```
**Tube Status**

As I rely on the DLR for my daily commute, it is important for me to have up-to-date information on the current tube status to ensure that I can plan my journey efficiently. By retrieving this information via an API and formatting it with a corresponding emoji, my dashboard provides a quick and easy way for me to stay informed about any potential disruptions or delays that may affect my commute. TFL have a variety of [API's](https://api.tfl.gov.uk/), but for my purposes I only wish to retrieve the [line status](https://api.tfl.gov.uk/swagger/ui/index.html?url=/swagger/docs/v1#!/Line/Line_Get). Their REST API is very simple to use and below is the code for retrieving this data and formatting it with an emoji

```python
def get_tube_status():
    app_key = st.secrets['TFL_KEY']
    url = f"https://api.tfl.gov.uk/Line/dlr/Status?detail=true&?app_key={app_key}"
    response = requests.get(url)
    response = response.json()
    dlr_status = response[0]['lineStatuses'][0]["statusSeverityDescription"]
    return dlr_status

def tube_status_emoji():
    dlr_status = get_tube_status()
    if 'Good' in dlr_status:
        dlr_status = '✅ ' + dlr_status
    elif 'Minor' in dlr_status:
        dlr_status = '⏰ ' + dlr_status
    elif 'Severe' or 'Suspended' in dlr_status:
        dlr_status = '⚠️ ' + dlr_status
    elif 'closure' in dlr_status:
        dlr_status = '⛔ ' + dlr_status
    return dlr_status

```

**Todays Work Tasks**

In my personal dashboard, I rely on ToDoist to retrieve my work-related tasks for the day. Unlike the personal section, which shows the percentage of completed tasks, ToDoist's API is called each time the page loads to provide me with an up-to-date list of work-related tasks. By retrieving the content of each task, I get a clear overview of the specific work-related tasks that I need to complete, helping me stay organized and focused throughout the day. This is achieved by creating a unique project and retrieving the contents of this via their API.

```python
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
```

**Next United Game**

As a lifelong fan of Manchester United, I never want to miss any of their games. To ensure that I am always up-to-date with the important information about the next match - including the date, time, whether it is a home or away game, the opponent, and the league - I use this football [API](https://rapidapi.com/api-sports/api/api-football/). This information is automatically retrieved and displayed as soon as the page is loaded, allowing me to stay on top of the latest fixtures

```python
def get_manutd_next_game_data():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    querystring = {"team":"33","next":"1"}
    headers = {"X-RapidAPI-Key": st.secrets['FOOTBALL_API_KEY'], "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response
    return response

def format_date(response):
        #splits date and time string in to two separate strings, one with just the date in, one with time
    date_and_time = (response.json())['response'][0]['fixture']['date']
    split_date = date_and_time.split('T')
        #gets time in format 00:00 hour:minutes but in 24hr format
    time = (split_date[1])[:5]
    date = split_date[0]
        #turns time to 12hr format
    format_time_24hr = datetime.strptime(time, '%H:%M')
    format_time_12hr = format_time_24hr.strftime('%I:%M %p')
        #change date to uk format (DD/MM/YY)
    format_date_with_datetime = (datetime.strptime(date, '%Y-%m-%d'))
    format_date_to_uk_format = format_date_with_datetime.strftime('%a-%d-%b')
    format_date_and_time = format_date_to_uk_format + ' @ ' + format_time_12hr
    return format_date_and_time

def extract_football_data(response, format_date_and_time):
    league = (response.json())['response'][0]['league']['name']
    home_team_name = (response.json())['response'][0]['teams']['home']['name']
    home_team_logo = (response.json())['response'][0]['teams']['home']['logo']
    away_team_name = (response.json())['response'][0]['teams']['away']['name']
    away_team_logo = (response.json())['response'][0]['teams']['away']['logo']
    match_teams = home_team_name + ' vs ' + away_team_name
    return match_teams, home_team_logo, away_team_logo, format_date_and_time, league

def football_api_process():
        response = get_manutd_next_game_data()
        format_date_and_time = format_date(response)
        football_widget = extract_football_data(response, format_date_and_time)
        return football_widget
football_widget = football_api_process()
```
**Data Pipeline Visualisation**

![alt text](images/welcomeimage.png)

---

*Rather than real-time data streaming, for this page and subsequent pages the pipeline is ran once nightly in a batch process*

<h2 align="center">Health Data</h2>

*The full code for my health data pipeline can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/Batch_Pipelines/Health-Data-Pipeline.py), the code for the frontend can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/pages/2%20_%F0%9F%A4%8D_Health.py)*

#### Pipeline One: Retrieving Steps, Active Calories, Total Calories Burned, Exercise, VO₂ Max & Diet

My apple watch tracks my movement and VO2 max but currently there is no easy direct access to automatically retrieve this data, so I figured a work-around. Starting with [this app](https://www.healthexportapp.com/) and an iOS Shortcut that runs once daily at night that aggregates and retrieves important data points and saves it to a CSV in my iCloud Drive I use [MyFitnessPal](https://www.myfitnesspal.com/) to track my diet. Although they have their own [API](https://myfitnesspalapi.com/), they are selective of who they give out API keys to, I have applied but have yet to receive a response. Nevertheless, Apple Health can connect to it for some basic metrics which is sufficient for my needs. I chose the most important diet metrics to me and included these in the daily data extraction. 


<div align="center">
	<img src="images/automatingshortcut.PNG" height =350  />
	 <img src="images/shortcut.PNG" height="350"  />
 </div>

Next step is to gain access to this file in my Python script, for this I use [PyiCloud]( https://github.com/picklepete/pyicloud). Once the file is accessible, I use python to extract and process the data. This data alongside the other health metrics is then added to my database CSV file ready to be visualised with Streamlit and Pandas. The code is as follows:

```python
class AppleHealthPipeline:

    def __init__(self):
        self.todays_date_only = str(datetime.datetime.today())[:10] 
        #- timedelta(1)))[:10]
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
```

#### Pipeline Two: Retrieving Sleep

Although in theory the above process should work for sleep data, I found it buggy - 50% of the time the sleep data was empty. However, what I use for my mood-tracker, [Exist]( https://exist.io/), has integrations with Apple Health, so getting sleep from their [API]( https://developer.exist.io/) was much more successful. When my python script runs each night, I use their REST API to get my sleep time, which goes directly to my CSV ready for visualisation with Stremalit and Pandas. The code is as follows: 

```python
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
```

#### Pipeline Three: Retrieving Body Metrics

For retrieval of my body measurements, I use a [Withings Smart-Scale]( https://www.withings.com/uk/en/scales), coupled with their [API]( https://developer.withings.co.uk/). I do a daily weigh-in which my Python script retrieves daily via their API. The data is then added to my CSV database for visualisation with Streamlit and Pandas. The code is as follows:

``` python
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
        today_start_of_day = today.replace(hour=00, minute=00, second=00, microsecond=00)
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
```

**Data Pipeline Visualisation**


<div align="center">
	<img src="images/healthimage.png"/>
 </div>

<h2 align="center">Productivity Data</h2>

*The full code for my productivity data pipeline can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/Batch_Pipelines/Productivity-Data-Pipeline.py), the code for the frontend can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/pages/3%20_%F0%9F%A4%8D_Productivity.py)*

#### Pipeline One: Retrieving Working & Reading Hours

For tracking my working and reading time I use [Tracking Time](https://trackingtime.co/), other viable options with API’s include [RescueTime](https://www.rescuetime.co.uk/) or [Toggl](https://toggl.co.uk/), but I prefer the interface of Tracking Time. Daily my Python script connects to their [API]( https://api.trackingtime.co/doc/index.html) and with a bit of processing, I can retrieve the time spent that day on reading and working respectively. This data is then added to my CSV and visualised with Streamlit and Pandas. Here is the code:

``` python
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

``` 

#### Pipeline Two: Retrieving Coding Hours

For a clearer picture on my productivity I installed [WakaTime]( https://wakatime.co.uk/) into my IDE to get the hours spent actually coding (which is a subset of my time spent working). Daily my Python script speaks to their [API]( https://wakatime.co.uk/developers) and adds this data to my CSV database for visualisation with Streamlit and Pandas. 

``` python
class WakaTimePipeline:

    def get_total_time_spent_coding_today(self):
        api_key = config('WAKATIME_API_KEY')
        url = f'https://wakatime.com/api/v1/users/gabriella01/summaries?api_key={api_key}&range=today'  
        response = requests.get(url)
        response = response.json()
        response = response['data'][0]['grand_total']
        time_in_decimal_format = response['decimal']
        return time_in_decimal_format
```

#### Pipeline Three: Retrieving GitHub Contributions

GitHub do have their own [API]( https://docs.github.co.uk/en/graphql) capable of retrieving this data but as I only care about commits at this moment, the [Exist]( https://exist.io/) – GitHub integration suffices. As above, my Python script connects to their [API]( https://developer.exist.io/) each night, retrieves this data and adds it to my CSV database for visualisation with Streamlit and Pandas. The code is as follows;

``` python
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
```

**Data Pipeline Visualisation**


<div align="center">
	<img src="images/productivityimage.png"/>
 </div>

<h2 align="center">Personal Data</h2>

*The full code for my personal data pipeline can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/Batch_Pipelines/Personal-Data-Pipeline.py), the code for the frontend can be viewed [here](https://github.com/gabriella-martin/Interactive-Dashboard/blob/main/pages/4%20_%F0%9F%A4%8D_Personal.py)*

#### Pipeline One: Retrieving ToDo's Done Data

I organise my daily life with [ToDoist]( https://todoist.com/), who have a great [API]( https://developer.todoist.com/guides/) where each night my Python script retrieves the percentage of tasks in each ToDoist section I have completed that day. I separate the task into sections by creating projects in ToDoist.  As the majority of my tasks are recurring, some manipulation with Python is necessary to accurately retrieve what has been completed today. These daily percentages are then added to my CSV database file for visualisation with Streamlit & Pandas. Here is the code:

```python
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

```

#### Pipeline Three: Retrieving Book Data

I have been an avid user of [Goodreads]( https://www.goodreads.com/user/show/108711145-gabriella-martin) to track my reading progress but although they did have a solid API, they have discontinued it and are no longer issuing keys. However, I use [Airtable]( https://airtable.com/) to store much of my personal data and began to add my book tracking data. I then could used their [API]( https://airtable.com/developers/web/api/introduction) to get my most recently read and currently reading books. Rather than being added daily to a CSV, this is instead called whenever the page is loaded in order to get an automatic update. The code is as follows:

``` python
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

```

#### Pipeline Four: Retrieving Listening Data

I use the Spotify [API]( https://developer.spotify.com/documentation/web-api/). There are many options for data to pull about your listening habits and I use a couple throughout the dashboard. Here I pull my recent top tracks so I can see what I have had on repeat recently. This is also not added to the CSV database and is again pulled automatically when the page is loaded