import requests
import sqlite3


def save_ea(sum_list):
    conn = sqlite3.connect("ea.db")
    c = conn.cursor()
    c.execute("CREATE TABLE ea (place TEXT, magnitude REAL)")
    c.executemany("INSERT INTO ea VALUES (?, ?)", sum_list)
    conn.commit()
    conn.close()


def print_ea():
    conn = sqlite3.connect("ea.db")
    c = conn.cursor()
    c.execute("SELECT * FROM ea")
    data = c.fetchall()
    for row in data:
        print(row)
    conn.commit()
    conn.close()


url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
start_time = input('Enter the start time: ')
end_time = input('Enter the end time: ')
latitude = input('Enter the latitude: ')
longitude = input('Enter the longitude: ')
max_radius_km = input('Enter the max radius in km: ')
min_magnitude = input('Enter the min magnitude: ')

response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': start_time,
    'endtime': end_time,
    'latitude': latitude,
    'longitude': longitude,
    'maxradiuskm': max_radius_km,
    'minmagnitude': min_magnitude
})

data = response.json()
earthquake_list = data['features']
sum_list = []
count = 0
for earthquake in earthquake_list:
    count += 1
    sum_list.append((earthquake['properties']['place'], earthquake['properties']['mag']))

save_ea(sum_list)
print_ea()
