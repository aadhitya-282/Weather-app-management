import requests


def get_weather(city):
    geocoding_url="https://geocoding-api.open-meteo.com/v1/search"
    params={
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
        }
    response=requests.get(geocoding_url, params=params)
    if response.status_code!=200:
        print("Unable to connect weather service.")
        return
    data=response.json()
    if "results" not in data:
        print("City not found")
        return
    location=data["results"][0]
    latitude=location["latitude"]
    longitude=location["longitude"]
    city_name=location["name"]
    weather_url="https://api.open-meteo.com/v1/forecast"
    weather_params={
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code"
        }
    weather_response=requests.get(weather_url, params=weather_params)
    if weather_response.status_code!=200:
        print("Unable to get weather information.")
        return
    weather_data=weather_response.json()
    current=weather_data["current"]
    return {
        "city": city_name,
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "feels_like": current["apparent_temperature"],
        "weather_code": current["weather_code"]
        }