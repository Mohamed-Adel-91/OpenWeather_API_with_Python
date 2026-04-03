import requests
import pandas as pd
import time

API_KEY = "f21accc8a43773e27af0525c31cfc7c8"
CITIES = ["Cairo", "Alexandria", "Riyadh", "London", "Tokyo", "InvalidCityName"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_batch_weather(city_list, app_id):
    weather_records = []
    
    print("Initiating batch data retrieval...")
    
    for city in city_list:
        params = {"q": city, "appid": app_id, "units": "metric"}
        
        try:
            response = requests.get(BASE_URL, params=params)
            
            if response.status_code == 200:
                data = response.json()
                
                record = {
                    "City": data['name'],
                    "Country": data['sys']['country'],
                    "Temperature_C": data['main']['temp'],
                    "Humidity_Pct": data['main']['humidity'],
                    "Wind_Speed_m_s": data['wind']['speed'],
                    "Condition": data['weather'][0]['main']
                }
                weather_records.append(record)
                print(f"[SUCCESS] Fetched payload for {city}")
                
            else:
                print(f"[ERROR] Failed to fetch {city}. HTTP Status: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"[FATAL] Connection error for {city}: {e}")
            
        time.sleep(0.5) 
        
    return weather_records

raw_data_list = fetch_batch_weather(CITIES, API_KEY)

df_current = pd.DataFrame(raw_data_list)

print("\n--- Batch Ingestion Complete ---")
print(df_current.head())


# Task 3: Data Processing and Exporting

features = ['City', 'Temperature_C', 'Humidity_Pct', 'Condition']
df_clean = df_current[features]

print("--- Extracted Key Data Points ---")
print(df_clean.head())

output_filename = "weather_data_export.csv"

df_clean.to_csv(output_filename, index=False, encoding='utf-8')

print(f"\n[SUCCESS] Pipeline execution complete. Dataset saved locally as '{output_filename}'.")