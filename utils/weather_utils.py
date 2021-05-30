from typing import List

import aiohttp
import requests
from aiocache import cached

from config import API_ADMIN_HOST
from model import WeatherMainAnswer, WeatherAnswer, WeatherClothes


@cached(ttl=5)
async def get_clothes_list(temp: float, weather_type: str) -> List[WeatherClothes]:
    async with aiohttp.ClientSession() as session:
        resp = await session.get(f"{API_ADMIN_HOST}/images?temp={temp}&weather_type={weather_type}")
        if resp.status == 200:
            json_data = await resp.json()
            return [WeatherClothes(**_data) for _data in json_data]
    return []


time_to_word = {
    '12:00:00': 'day',
    '15:00:00': 'day',
    '18:00:00': 'evening',
    '21:00:00': 'evening',
    '00:00:00': 'night',
    '03:00:00': 'night',
    '06:00:00': 'morning',
    '09:00:00': 'morning',
}
icon_src = {
    '01d': 'http://openweathermap.org/img/wn/01d@2x.png',
    '02d': 'http://openweathermap.org/img/wn/02d@2x.png',
    '03d': 'http://openweathermap.org/img/wn/03d@2x.png',
    '04d': 'http://openweathermap.org/img/wn/04d@2x.png',
    '09d': 'http://openweathermap.org/img/wn/09d@2x.png',
    '10d': 'http://openweathermap.org/img/wn/10d@2x.png',
    '11d': 'http://openweathermap.org/img/wn/11d@2x.png',
    '13d': 'http://openweathermap.org/img/wn/13d@2x.png',
    '50d': 'http://openweathermap.org/img/wn/50d@2x.png',
    '01n': 'http://openweathermap.org/img/wn/01n@2x.png',
    '02n': 'http://openweathermap.org/img/wn/02n@2x.png',
    '03n': 'http://openweathermap.org/img/wn/03n@2x.png',
    '04n': 'http://openweathermap.org/img/wn/04n@2x.png',
    '09n': 'http://openweathermap.org/img/wn/09n@2x.png',
    '10n': 'http://openweathermap.org/img/wn/10n@2x.png',
    '11n': 'http://openweathermap.org/img/wn/11n@2x.png',
    '13n': 'http://openweathermap.org/img/wn/13n@2x.png',
    '50n': 'http://openweathermap.org/img/wn/50n@2x.png'
}


def get_icon_src(icon: str) -> str:
    return icon_src[icon]




def round_lat_lon(lat: float, lon: float):
    return round(lat, 1), round(lon, 1)
