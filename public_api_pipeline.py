
import requests 
import pickle
import datetime
import streamlit as st
from datetime import datetime
from decouple import config 

'''def get_manutd_next_game_data():
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


with open('footie', 'wb') as fb:
    pickle.dump(football_widget, fb)'''

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

def get_condition_emoji():
    description = get_weather()[3]
    if 'Thunderstorm' in description:
        condition_emoji = '⚡'
    elif 'Drizzle' in description:
        condition_emoji ='💧'
    elif 'Rain' in description:
        condition_emoji ='🌧️'
    elif 'Snow' in description:
        condition_emoji ='❄️'
    elif 'Clear Sky' in description:
        condition_emoji = '🌤'
    elif 'Clouds' in description:
        condition_emoji ='️🌥'
    else:
        condition_emoji = '🌫️'
        
    return condition_emoji


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



def nasa_image_of_the_day():
    url = 'https://api.nasa.gov/planetary/apod?api_key=PZcnX4xvaDZt6n394qdhjTT9p9Jvwex3oTqMofpt'
    response = requests.get(url)
    nasa_image = (response.json())['hdurl']
    return nasa_image