from decouple import config 
from datetime import datetime
import requests 


def get_manutd_next_game_data():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    querystring = {"team":"33","next":"1"}
    headers = {"X-RapidAPI-Key": config('FOOTBALL_API_KEY'), "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers, params=querystring)
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
    format_date_to_uk_format = format_date_with_datetime.strftime('%a-%d-%B')

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
