import requests
import time

API_KEY = "5c1a7e28c59cf9d9ddf0c7b68f465464"

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Use Celsius for temperature
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return None

def display_weather(city):
    weather_data = get_weather(city)
    if weather_data:
        print(f"Weather in {city}: {weather_data['weather'][0]['description']}, Temperature: {weather_data['main']['temp']}°C")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    city = input("Enter a city: ")
    while True:
        display_weather(city)
        time.sleep(15)  # Sleep for 15 seconds before refreshing
