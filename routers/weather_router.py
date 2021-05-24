import json
from datetime import datetime
from enum import Enum
from typing import Optional
from urllib import request

import aiohttp
from fastapi import APIRouter, Query

from config import API_WEATHER_HOST, API_KEY, DATETIME_F
from schemas import WeatherAnswer, WeatherMainAnswer

weather_router = APIRouter(tags=['Погода'], prefix='/weather')

time_to_word = {
    '15:00:00': 'день',
    '09:00:00': 'утро',
    '21:00:00': 'вечер',
    '03:00:00': 'ночь',
}


@weather_router.get('/', response_model=WeatherMainAnswer)
async def get_weather_city(city: str = Query(None, title='Город', description='Название города', example='Москва'),
                           lat: float = Query(None, title='Широта', description='Широта', example=160.321, lt=360),
                           lon: float = Query(None, title='Долгота', description='Широта', example=60.123, lt=360),
                           now_datetime: str = Query(datetime.now().strftime(DATETIME_F), title='Долгота',
                                                     description='Широта', example='2021-13-25 01:13:20')):
    async with aiohttp.ClientSession() as session:
        if city is not None:
            resp = await session.get(f'{API_WEATHER_HOST}/data/2.5/forecast?q={city}&appid={API_KEY}')
        if lat is not None and lon is not None:
            resp = await session.get(f'{API_WEATHER_HOST}/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}')
        if resp is not None:
            data = await resp.json()
            # day_weather_list = [weather for weather in data['list'] if str(weather['dt_txt']).endswith('15:00:00')]
            day_weather_list = []
            for weather in data['list']:
                datetime.strptime(weather['dt_txt'], DATETIME_F)
                datetime_spl = weather['dt_txt'].split(' ')
                date = datetime_spl[0]
                time = datetime_spl[1]

                if time == '15:00:00':  # day
                    weather.update(weather['main'])
                    weather['weather'] = weather['weather'][0]
                    weather['date'] = date
                    weather['time'] = time
                    weather['dt_txt_info'] = time_to_word[time]
                    day_weather_list.append(WeatherAnswer(**weather))

            return WeatherMainAnswer(list=day_weather_list)

# @weather_router.get('/')
# async def get_weather_lat_lon(lat: Optional[float], lon: Optional[float]):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f'{API_WEATHER_HOST}/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}') as resp:
#             data = await resp.json()
#             print(data)
