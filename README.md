# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: VINDHYA H K

*INTERN ID*: CT08WOV

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH


OUTPUT:








Weather Dashboard Project:


A simple Python application that fetches weather forecast data from the OpenWeatherMap API and visualizes it using matplotlib.

Features

- Retrieves 5-day weather forecast data for any city
- Creates visualizations for temperature and humidity
- Saves the dashboard as a PNG file
- Displays statistical information about the forecast

Installation

1. Clone this repository or download the script
2. Install the required Python packages:


pip install requests matplotlib pandas python-dotenv


API Key Setup

1. Create a free account at [OpenWeatherMap](https://openweathermap.org/api)
2. Generate an API key
3. Create a `.env` file in the same directory as the script with the following content:


OPENWEATHER_API_KEY=your_api_key_here


Usage

Run the script with Python:

python weather_dashboard.py

When prompted, enter the name of a city to generate the weather forecast dashboard.
The script will:
1. Generate a visualization with two charts:
   - Temperature forecast (actual and "feels like")
   - Humidity forecast
2. Save the visualization as `[city_name]_weather_dashboard.png`
3. Display basic statistics in the console:
   - Average temperature
   - Maximum temperature
   - Minimum temperature
   - Average humidity


If using VSCode, make sure you've selected the correct Python interpreter where packages are installed.

Future Enhancements

- Add more weather metrics (wind speed, precipitation, etc.)
- Implement a web-based dashboard using Dash or Streamlit
- Add functionality to compare weather between multiple cities
- Create historical weather data visualizations

License

This project is open source and available under the MIT License.
