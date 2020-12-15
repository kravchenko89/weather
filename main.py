import requests
import configparser


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather(zip_cod, api_key):

    api_url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_cod}&appid={api_key}&mode=json&units=metric"
    request = requests.get(api_url)
    print(request)
    return request.json()


print(get_weather('95129', get_api_key()))
