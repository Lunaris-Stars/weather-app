import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "146736f3c92acaef9fda7cd02e5c90f1"

CITY = input("enter the city name :  ")

url  = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(url=url).json()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9.5) + 32
    return celsius , fahrenheit

TEMP_KELVIN = response['main']['temp']
TEMP_CELSIUS , TEMP_FAHRENHEIT = kelvin_to_celsius_fahrenheit(TEMP_KELVIN)

HUMIDITY = response['main']['humidity']
WIND_SPEED = response['wind']['speed']
DESCRIPTION = response['weather'][0]['description']

COUNTRY = response['sys']['country']
SUNRISE = response['sys']['sunrise']
SUNSET = response['sys']['sunset']

print(f"Weather in {CITY}, {COUNTRY}:")
print(f"  Temperature: {TEMP_CELSIUS:.2f}°C / {TEMP_FAHRENHEIT:.2f}°F")
print(f"  Humidity: {HUMIDITY}%")
print(f"  Wind Speed: {WIND_SPEED} m/s")
print(f"  Description: {DESCRIPTION}")
print(f"  Sunrise: {SUNRISE}")
print(f"  Sunset: {SUNSET}")