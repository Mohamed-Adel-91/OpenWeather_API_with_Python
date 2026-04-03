import requests
import pandas as pd

API_KEY = "f21accc8a43773e27af0525c31cfc7c8"
CITY = "Cairo"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

print(f"Initiating GET request to OpenWeather for {CITY}...")
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    weather_data = response.json()
    
    current_temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    
    print(f"Success. Current Temp: {current_temp}°C, Humidity: {humidity}%, Condition: {description}")

    df = pd.json_normalize(weather_data)
    print("\nData loaded into Pandas DataFrame successfully.")
    
else:
    print(f"Error fetching data. HTTP Status Code: {response.status_code}")
    print(response.text)