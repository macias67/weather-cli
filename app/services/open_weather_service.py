import requests
from dotenv import dotenv_values
from requests import Response

from app.models.city import City

env = dotenv_values(".env")

BASE_URL_WEATHER_API = env["BASE_URL_WEATHER_API"]
WEATHER_API_KEY = env["WEATHER_API_KEY"]


def fetch_data(city_name: str) -> Response:
    status_code = 0
    try:
        response = requests.get(
            BASE_URL_WEATHER_API + "/data/2.5/forecast",
            params={"q": city_name, "cnt": 4, "lang": "es", "appid": WEATHER_API_KEY},
            headers={'Accept': 'application/json'}
        )
        status_code = response.status_code
        response.raise_for_status()
    except requests.HTTPError:
        raise SystemExit("HTTP error, status code {}".format(status_code))
    except requests.RequestException as err:
        raise SystemExit("Ops, something went wrong... {}".format(err))

    return response


def get_city_weather(city_name: str) -> City:
    weather_data = fetch_data(city_name)
    city = City(weather_data.json())

    return city
