from pprint import pprint
import requests


def get_weather(city_name):
    """
    Fetches weather information for a given city using the OpenWeatherMap API.

    Parameters:
    city_name (str): The name of the city to get weather information for.

    Returns:
    A dictionary containing various weather-related data such as temperature,
    humidity, pressure, sunrise and sunset times, and a brief description of the weather.
    If there is an error fetching the data, returns False.
    """
    # Set up API key, base URL, and query parameters
    api_key = "API_KEY"
    url = "https://api.openweathermap.org/data/2.5/weather"
    query_params = {
        'q': city_name,
        'units': "metric",
        'appid': api_key
    }

    # Send GET request to API and check response status code
    response = requests.get(url, params=query_params)
    if response.status_code == 200:
        # Parse JSON response and extract relevant weather data
        data = response.json()
        info = {
            "city name": data['name'],
            "country": data['sys']['country'],
            "latitude": data['coord']['lat'],
            "longitude": data['coord']['lon'],
            "description": data['weather'][0]['description'],
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "pressure": data['main']['pressure'],
            'sunrise': data['sys']['sunrise'],
            'sunset': data['sys']['sunset'],
            "icon": data["weather"][0]["icon"],
            "icon_url": f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@4x.png"
        }
        return info
    else:
        print(f"Error fetching weather data: {response.status_code} {response.reason}")
        return False


if __name__ == "__main__":
    # Prompt user to enter city name and fetch weather data
    city_name = input("Enter the city name: ")
    weather_data = get_weather(city_name)

    if weather_data:
        # Print weather data using pprint
        for key, value in weather_data.items():
            if 'icon' in key:
                continue
            pprint(f"{key:>30} = {value}")
    else:
        print("No weather data available.")
