from model import WeatherMainAnswer
from utils.weather_utils import round_lat_lon, get_clothes_list, get_icon_src, time_to_word
from weather_api import api


async def get_lat_lon(lat: float, lon: float):
    lat, lon = round_lat_lon(lat, lon)
    resp = await api.get_lat_lon(lat, lon)
    return await get_weather(json_data=await resp.json())


async def get_city(city):
    resp = await api.get_city(city)
    return await get_weather(json_data=await resp.json())



async def get_weather(json_data: dict) -> WeatherMainAnswer:
    weather_json_list = json_data['list']
    day_weather_now = weather_json_list[1]['dt_txt'].split(' ')[0]
    day_weather_list = [await json_weather_to_model(weather_json_list[1])]
    weather_json_list = weather_json_list[2:]
    for weather in weather_json_list:
        spl = weather['dt_txt'].split(' ')
        date = spl[0]
        time = spl[1]
        if day_weather_now == date:
            continue
        if time == '15:00:00':  # day
            day_weather_list.append(await json_weather_to_model(weather))
    json_data['list'] = day_weather_list
    return WeatherMainAnswer(**json_data)



async def json_weather_to_model(weather: dict) -> dict:
    time = weather['dt_txt'].split(' ')[1]
    weather['weather'] = weather['weather'][0]
    weather['time_txt_info'] = time_to_word[time]
    weather['weather']['clothes_list'] = await get_clothes_list(temp=weather['main']['feels_like'], weather_type=weather['weather']['main'])
    weather['weather']['icon_src'] = get_icon_src(weather['weather']['icon'])
    return weather
