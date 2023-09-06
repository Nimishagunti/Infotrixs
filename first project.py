import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Use Celsius for temperature
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return None

if __name__ == "__main__":
    city = input("Enter a city: ")
    api_key = "5c1a7e28c59cf9d9ddf0c7b68f465464"
    weather_data = get_weather(city, api_key)
    if weather_data:
        print(f"Weather in {city}: {weather_data['weather'][0]['description']}, Temperature: {weather_data['main']['temp']}°C")
    else:
        print("Weather data not available.")
