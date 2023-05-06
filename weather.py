
import datetime as dt
import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = ''
CITY = ""

def kelvin_to_celcius(kelvin):
    celcius  = kelvin -273.15
    return celcius


response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}').json()


temp_kelvin = response['main']['temp']
temp_celcius = kelvin_to_celcius(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celcius = kelvin_to_celcius(feels_like_kelvin)

temp_min_kelvin = response['main']['temp_min']
temp_max_kelvin = response['main']['temp_max']
temp_min_celcius = kelvin_to_celcius(temp_min_kelvin)
temp_max_celcius = kelvin_to_celcius(temp_max_kelvin)

humity = response['main']['humidity']
temp_min = response['main']['temp_min']
description = response['weather'][0]['description']
sunrise_time = response['sys']['sunrise'] + response['timezone']

print("************************************")
print(f"Temperature is: {temp_celcius:.2f}℃")
print(f"Feels like: {feels_like_celcius:.2f}℃")
print(f"General weather: {description}")
print(f"Min Temp: {temp_min_celcius:.2f}℃")
print(f"Max Temp: {temp_max_celcius:.2f}℃")
