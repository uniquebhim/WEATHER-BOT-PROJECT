# WeatherBot

WeatherBot is a Python program that fetches the current weather information of a given city from the OpenWeatherMap API and displays it in a formatted manner. It provides information like temperature, humidity, pressure, sunrise, sunset, latitude, longitude, and weather description.

## Prerequisites

To run WeatherBot, you need to have Python 3.x installed on your system. You also need to install the **`requests`** module by running the following command in your terminal:

```
pip install requests

```

## Usage

To use WeatherBot, run the **`weather_bot.py`** file using Python and enter the name of the city for which you want to know the weather information. For example:

```
python weather_bot.py
Enter the City Name: London

```

The program will then fetch the current weather information for London and display it in the following format:

```
City Name = London
Country = GB
Lat = 51.5085
Lon = -0.1257
Desc = broken clouds
Temp = 9.47°C
Humidity = 81%
Pressure = 1026 hPa
Sunrise = 1657746975
Sunset = 1657800786
Icon URL = <https://openweathermap.org/img/wn/04n@4x.png>

```

If the program cannot fetch the weather information for the specified city, it will display an error message.

## License

WeatherBot is licensed under the **[MIT License](https://github.com/yourusername/weather_bot/blob/main/LICENSE)**.

## Acknowledgements

WeatherBot was created using the **[OpenWeatherMap API](https://openweathermap.org/api)**.
