<h2 align="center">Interactive Dashboard</h2>

----
<h4 align="center">Languages and Technologies</h4>

<div align="center">
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" height="40" width="52"   />
	 <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="40" width="52"  />
	<img src="https://toppng.com/uploads/preview/rest-api-icon-rest-api-icon-11553510526uqs2ynyga2.png" alt="html5" width="40" height="40"/>
	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apple/apple-original.svg"  width="40" height="40"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="40" width="52"   />
    <img src="https://avatars.githubusercontent.com/u/45109972?s=280&v=4" height="40" width="52"   />
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Matplotlib_icon.svg/2048px-Matplotlib_icon.svg.png" height="40" width="52"   /> </div>


## Introduction
As someone who loves collecting data on my daily life, I was motivated by the need to simplify the often cumbersome process of accessing and analyzing data that plays a crucial role in my daily life. Before creating this dashboard, I found myself frequently jumping between multiple apps and sources of information just to gather the data I needed to make informed decisions about my health, work, and other important aspects of my life.

Not only was this approach inefficient and time-consuming, but it also made it difficult to get a complete and holistic view of the data I was dealing with. It was a challenge to track trends over time, identify patterns, and draw meaningful insights from the information at my disposal. In short, the lack of a centralized, user-friendly platform for managing my personal data was hindering my ability to live a more organized, productive, and fulfilling life.

That's where this app comes in. By consolidating all of my personal data in one place and presenting it in a visually appealing and intuitive manner, this dashboard has made it much easier for me to monitor my progress, identify areas for improvement, and stay on top of the things that matter most to me; this app has become an indispensable tool for helping me stay organized, focused, and in control of my life.

I began by making a list of metrics I wanted to track in four core categories; general, health, personal and productivity. I dedicated a page to each of these categories in my dashboard

To view the dashboard (with dummy data for privacy), go to this [link](https://gabriella-martin-interactive-dashboard-welcome-9hpibj.streamlit.app/)

**Dashboarding Software**

Streamlit is a Python library that I chose to use for building my dashboard because of its simplicity, flexibility, and ease of use. I also chose to use Streamlit because I wanted to focus on improving my backend development skills while still being able to create a polished and user-friendly frontend for my dashboard. Streamlit provided an ideal solution to this challenge by enabling me to quickly build a professional-looking dashboard without requiring extensive knowledge of front-end development. This allowed me to focus more on the data processing and analysis that is critical to my project while still delivering a polished and responsive user experience. If you are a Python user, check it out [here]( https://docs.streamlit.io/)!


### Welcome Page

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

![alt text](welcomeimage.png)

