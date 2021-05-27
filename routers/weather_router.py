import aiohttp
from fastapi import APIRouter, Query

from config import API_WEATHER_HOST, API_KEY
from model import WeatherMainAnswer

from utils.weather_utils import get_weather
from weather_api.api import round_lat_lon, get_open_lat_lon

weather_router = APIRouter(tags=['Погода'], prefix='/weather')


@weather_router.get('/', response_model=WeatherMainAnswer)
async def get_weather_city(city: str = Query(None, title='Город', description='Название города', example='Москва'),
                           lat: float = Query(None, title='Широта', description='Широта', example=60.321, lt=360),
                           lon: float = Query(None, title='Долгота', description='Широта', example=30.123, lt=360)):

    if city is not None:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(f'{API_WEATHER_HOST}/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}')
            return get_weather(json_data=await resp.json())
    if lat is not None and lon is not None:
        lat, lon = round_lat_lon(lat, lon)
        resp = await get_open_lat_lon(lat, lon)
        return get_weather(json_data=await resp.json())
