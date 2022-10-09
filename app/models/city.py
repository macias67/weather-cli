from dataclasses import dataclass

from typing import List


@dataclass
class Weather:
    def __init__(self, id_weather: int, main: str, description: str) -> None:
        self.id_weather: id_weather
        self.main: main
        self.description: description


@dataclass
class WeatherHour:
    def __init__(self, dt_txt: str, temp: float, temp_min: float, temp_max: float, humidity: int, weather: Weather):
        self.dt_txt = dt_txt
        self.temp = temp
        self.temp_min: temp_min
        self.temp_max: temp_max
        self.humidity: humidity
        self.weather: weather


@dataclass
class City:
    id_city: int
    name: str
    coords: dict
    hours: List[WeatherHour]

    def __init__(self, data: dict):
        self.id_city = data["city"]["id"]
        self.name = data["city"]["name"]
        self.coords = data["city"]["coord"]

        list_hours = []
        for weather_hour in data["list"]:
            weather = Weather(
                id_weather=weather_hour["weather"][0]["id"],
                main=weather_hour["weather"][0]["main"],
                description=weather_hour["weather"][0]["description"]
            )
            weather_hour = WeatherHour(
                dt_txt=weather_hour["dt_txt"],
                temp=weather_hour["main"]["temp"],
                temp_min=weather_hour["main"]["temp_min"],
                temp_max=weather_hour["main"]["temp_max"],
                humidity=weather_hour["main"]["humidity"],
                weather=weather
            )
            list_hours.append(weather_hour)

        self.hours = list_hours
