import sqlite3
import json


conn = sqlite3.connect('database.sql')
cn = conn.cursor()
cn.execute('CREATE TABLE IF NOT EXISTS cities(count TEXT, city TEXT)')


with open('countries.json', 'r') as countries:
    datas = json.load(countries)
    for country in datas:
        for city in datas[country]:
            cn.execute('INSERT INTO cities VALUES(?,?);', (country, city))

        conn.commit()

conn.close()
