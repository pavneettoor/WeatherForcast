import requests
from dataclasses import dataclass
from config.config import API_KEY

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int
    air_pollution_index: int

def get_weather_coordinates(city_name, state_code, country_code, api_key):
    api_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}"
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    lat, lon = data[0].get("lat"), data[0].get("lon")
    return lat, lon

def get_air_pollution_index(lat, lon, api_key):
    air_pollution_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(air_pollution_url)
    response.raise_for_status()
    air_pollution_data = response.json()
    return air_pollution_data.get("list")[0].get("main").get("aqi")

def get_current_weather(lat, lon, api_key):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(api_url)
    response.raise_for_status()
    api_data = response.json()

    air_pollution_index = get_air_pollution_index(lat, lon, api_key)

    data = WeatherData(
        main=api_data.get("weather")[0].get("main"),
        description=api_data.get("weather")[0].get("description"),
        icon=api_data.get("weather")[0].get("icon"),
        temperature=int(api_data.get("main").get("temp")),
        air_pollution_index=air_pollution_index
    )

    return data

def main(city_name, state_code, country_code):
    lat, lon = get_weather_coordinates(city_name, state_code, country_code, API_KEY)
    weather_data = get_current_weather(lat, lon, API_KEY)
    return weather_data

if __name__ == "__main__":
    city_name = "Toronto"
    state_code = "ON"
    country_code = "CA"
    print(main(city_name, state_code, country_code))
