import requests
import json
import configparser

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
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
    app.run()
