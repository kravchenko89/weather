import requests
import configparser
from flask import render_template


def data_weather(data):
    temp = f"{float(data['main']['temp'])}"
    feels_like = '{0:.2f}'.format(data['main']['feels_like'])
    weather = data['weather'][0]['main']
    location = data['name']

    return render_template('results.html', location=location, temp=temp,
                           feels_like=feels_like, weather=weather)


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api_key']


def get_weather(city_name, api_key):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}&mode=json&units=metric"
    request_q = requests.get(api_url)
    return request_q.json()

