import sys
import subprocess

required_packages = ['requests', 'matplotlib', 'pandas', 'python-dotenv', 'seaborn']
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f"{package} installed successfully!")


import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# OpenWeatherMap API
API_KEY = "8e0565c04b22b66905f1d4534271f9ad"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CITY = "New Delhi"  # Change this to your preferred city

# Fetch weather data
def fetch_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data")
        return None

# Process data
def process_data(data):
    if not data:
        return None
    
    main = data["main"]
    wind = data["wind"]
    weather_info = {
        "City": data["name"],
        "Temperature (°C)": main["temp"],
        "Humidity (%)": main["humidity"],
        "Pressure (hPa)": main["pressure"],
        "Wind Speed (m/s)": wind["speed"]
    }
    return pd.DataFrame([weather_info])

# Visualization
def visualize_data(df):
    plt.figure(figsize=(10, 5))
    sns.barplot(x=df.columns[1:], y=df.iloc[0, 1:])
    plt.title(f"Weather Data for {df['City'][0]}")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    weather_data = fetch_weather_data(CITY)
    df = process_data(weather_data)
    if df is not None:
        print(df)
        visualize_data(df)
    else:
        print("No data to visualize")
