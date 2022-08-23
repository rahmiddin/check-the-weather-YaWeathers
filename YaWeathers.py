import os
import requests
from geopandas.tools import geocode
from dotenv import load_dotenv

load_dotenv()


class YaWeather:

    def __init__(self, key):
        self.key = key

    def get_headers(self):

        return {
            'X-Yandex-API-Key': f'{self.key}'
        }

    def calculating_lat_lon_(self):

        # address we need to locate
        loc = os.environ.get('LOCATIONS')

        # finding the location
        location = geocode(loc, provider="nominatim", user_agent='my_request')
        point = location.geometry.iloc[0]

        lat = point.y
        lon = point.x


        return lat, lon

    def get_weathers(self):
        headers = self.get_headers()
        lat, lon = self.calculating_lat_lon_()
        url = f'https://api.weather.yandex.ru/v2/informers?'
        params = {'lat': lat, 'lon': lon, 'lang': 'ru_UA'}
        response = requests.get(url, headers=headers, params=params)
        return response.json()




