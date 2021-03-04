import sqlite3

from flask import Flask, render_template, request

from function import data_weather, get_api_key, get_weather


app = Flask(__name__)

conn = sqlite3.connect('database.sql', check_same_thread=False)
cur = conn.cursor()

api_key = get_api_key()


@app.route('/')
def weather_dashboard():
    cur.execute("SELECT * FROM cities ORDER BY count")
    data = cur.fetchall()

    return render_template('home.html', data=data)


@app.route('/results', methods=['POST'])
def render_results():
    city = request.form['City']

    data = get_weather(city, api_key)
    return data_weather(data)


@app.route('/resultss/<city>/', methods=['GET'])
def render_press(city):
    data = get_weather(city, api_key)
    return data_weather(data)


if __name__ == '__main__':
    app.run(debug=True)
