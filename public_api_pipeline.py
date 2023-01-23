from decouple import config 
from datetime import datetime
import requests 


'''def get_manutd_next_game_data():
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    querystring = {"team":"33","next":"1"}
    headers = {"X-RapidAPI-Key": config('FOOTBALL_API_KEY'), "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    reponse = response
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
        return football_widget'''


'''def get_weather():

    lat = 51.4676
    lon = 0.0169
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid=0d2c3100756b9fcb889310eef0183073'
    response = requests.get(url)
    print(response.json())



get_weather()'''

'''def get_weather():

    APIkey = config('WEATHER_API_KEY')
    resource = 'val/wxobs/all/json/sitelist'
    url = f'http://datapoint.metoffice.gov.uk/public/data/{resource}?key={APIkey}'
    response = requests.get(url)
    print(response)


get_weather()'''

'''def get_weather():
    api_key = config('WEATHER_API_KEY')
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=London&days=1'
    response = (requests.get(url)).json()
    degree_sign = u'\N{DEGREE SIGN}'

    current_temp = str(response['current']['temp_c'])
    current_feels_like = str(response['current']['feelslike_c'])
    temperature_text = current_temp + degree_sign + ' | Feels Like: ' + current_feels_like + degree_sign
    current_condition = str(response['current']['condition']['text'])
    current_wind = str(response['current']['wind_kph'])
    current_rain = str(response['forecast']['forecastday'][0]['day']['daily_will_it_rain'])

    if current_rain == '0':
        current_rain = 'No'
    else:
        current_rain = 'Yes'

    wind_rain_text = 'Wind: ' + current_wind + ' | ' +  'Rain: ' + current_rain
    sunrise = str(response['forecast']['forecastday'][0]['astro']['sunrise'])
    sunset = str(response['forecast']['forecastday'][0]['astro']['sunset'])

    sunrise_text = 'Sunrise: ' + sunrise  
    sunset_text =  'Sunset: ' + sunset 

    weather_text = temperature_text + '\n' + current_condition + '\n' + wind_rain_text + '\n' + sunrise_text + '\n' + sunset_text

    return weather_widget'''
