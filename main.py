import requests
import json
import configparser
import sqlite3

from flask import Flask, render_template, request
from flask_caching import Cache


cache = Cache(config={'CACHE_TYPE': 'simple'})
app = Flask(__name__)
cache.init_app(app)

conn = sqlite3.connect('database.db')
c = conn.cursor()


@app.route('/')
@cache.cached(timeout=300)
def weather_dashboard():
    with open('countries.json', 'r') as countries:
        datas = json.load(countries)
    return render_template('home.html', datas=datas)


@app.route('/results', methods=['POST'])
def render_results():
    city_name = request.form['City']
    api_key = get_api_key()
    data = get_weather(city_name, api_key)
    # temp = '{0:.2f}'.format(data['main']['temp'])
    temp = f"{float(data['main']['temp'])}"
    feels_like = '{0:.2f}'.format(data['main']['feels_like'])
    weather = data['weather'][0]['main']
    location = data['name']

    return render_template('results.html', location=location, temp=temp,
                           feels_like=feels_like, weather=weather)


@app.route('/resultss/<city>/', methods=['GET'])
def City(city):
    # import pdb
    # pdb.set_trace()
    api_key = get_api_key()
    data = get_weather(city, api_key)
    temp = f"{float(data['main']['temp'])}"
    feels_like = '{0:.2f}'.format(data['main']['feels_like'])
    weather = data['weather'][0]['main']
    location = data['name']
    return render_template('results.html', location=location, temp=temp,
                           feels_like=feels_like, weather=weather)


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather(city_name, api_key):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}&mode=json&units=metric"
    request_q = requests.get(api_url)
    return request_q.json()


if __name__ == '__main__':
    app.run(debug=True)

#  TODO 1 caching cities
#       2 view
