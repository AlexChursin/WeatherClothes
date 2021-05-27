from typing import List

from pydantic import BaseModel, Field


class Main(BaseModel):
    temp: float = Field(..., description='средняя температура, С', title='температура', example=14)
    feels_like: float = Field(..., description='температура по ощущениям, С', title='температура', example=16)
    temp_min: float = Field(..., description='мин. температура, C', title='температура', example=14)
    temp_max: float = Field(..., description='макс. температура, C', title='температура', example=19)
    humidity: int = Field(..., description='атмосферное давление, %', title='давление', example=84)
    pressure: int = Field(..., description=' Atmospheric pressure on the sea level, hPa', title='давление',
                          example=1018)
    temp_kf: float


class WeatherItem(BaseModel):
    main: str = Field(..., description='описание', title='тип погоды', example='Rain')
    description: str = Field(..., description='подробное описание', title='тип погоды', example='light rain')
    clothes_list: List[str] = Field(..., description='фотографии одежды под погоду', title='список ссылок на фото',
                                    example=['https://daily...imag1.png',
                                             'https://daily...imag2.png',
                                             'https://daily...imag3.png',
                                             'https://daily...imag4.png', ])
    icon: str = Field(..., description='название картинки', title='картинка погоды',
                      example='02d')
    icon_src: str = Field(..., description='ссылка на картинку', title='картинка погоды',
                          example='http://openweathermap.org/img/wn/02d@2x.png')


class WeatherAnswer(BaseModel):
    dt: int = Field(..., description='timestamp', title='timestamp', example=1621868400)
    main: Main = Field(..., description='числовая информация', title='погода')
    weather: WeatherItem = Field(..., description='текстовая информация', title='погода')
    dt_txt: str = Field(..., description='дата прогноза', title='дата время', example='2021-05-26 15:00:00')
    time_txt_info: str = Field(..., description='утро/день/вечер/ночь', title='время прогноза словами',
                               example='evening')


class Coord(BaseModel):
    lat: float
    lon: float


class City(BaseModel):
    id: int
    name: str = Field(..., description='название города')
    coord: Coord = Field(..., description='координаты')
    country: str = Field(..., description='страна')
    population: int = Field(..., description='численность')
    timezone: int = Field(..., description='временная зона')
    sunrise: int = Field(..., description='рассвет, timestamp')
    sunset: int = Field(..., description='закат, timestamp')


class WeatherMainAnswer(BaseModel):
    list: List[WeatherAnswer] = Field(..., description='список погоды: сейчас/завтра/послезавтра/п-послезавтра')
    city: City = Field(..., description='информация о городе')
