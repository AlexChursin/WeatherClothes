import aiohttp
from fastapi import APIRouter, Query

from config import API_WEATHER_HOST, API_KEY
from model import WeatherMainAnswer

from providers import weather_provider
weather_router = APIRouter(tags=['Погода'], prefix='/weather')


@weather_router.get('/', response_model=WeatherMainAnswer)
async def get_weather(city: str = Query(None, title='Город', description='Название города', example='Москва'),
                           lat: float = Query(None, title='Широта', description='Широта', example=60.321, lt=360),
                           lon: float = Query(None, title='Долгота', description='Широта', example=30.123, lt=360)):

    if city is not None:
        return await weather_provider.get_city(city)
    if lat is not None and lon is not None:
        return await weather_provider.get_lat_lon(lat, lon)
