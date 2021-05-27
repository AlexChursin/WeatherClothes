from model import WeatherMainAnswer, WeatherAnswer


def get_clothes_list(temp: float):
    return [
        'https://dailydressme.com/_next/image?url=https%3A%2F%2Fdailydressme.com%2Fassets%2F200x%2Cq90%2Fa8652e41d5a36116c72d44ae302ef151%2Fd0ed21d6%2FIgorTurtleneckTHEUPSIDEbrand-THEUPSIDE.jpg&w=3840&q=75',
        'https://dailydressme.com/_next/image?url=https%3A%2F%2Fdailydressme.com%2Fassets%2F200x%2Cq90%2F4b9f0c33d9e0e1375a92cedc9d74ed1f%2F1e936e0e%2FSabinaJumpsuitLVHRbrand-LVHR.jpg&w=3840&q=75',
        'https://dailydressme.com/_next/image?url=https%3A%2F%2Fdailydressme.com%2Fassets%2F200x%2Cq90%2Fdfa980fd753e06f83c08e255d28c3e6b%2F9ee874dd%2FTheBrooklynSweatpantCOTTONCITIZENbrand-COTTONCITIZEN.jpg&w=3840&q=75',
        'https://dailydressme.com/_next/image?url=https%3A%2F%2Fdailydressme.com%2Fassets%2F200x%2Cq90%2F48f0093ee7d5a56f88d10d1d8612b419%2Fba2a39af%2FPufferJacketChampionbrand-Champion.jpg&w=3840&q=75',
        'https://dailydressme.com/_next/image?url=https%3A%2F%2Fdailydressme.com%2Fassets%2F200x%2Cq90%2F812d09c0b6c04412d28a9d768a9e7368%2Fd162f660%2FPlutoPufferJacketToastSocietybrand-ToastSociety.jpg&w=3840&q=75',
        'https://dailydressme.com/_next/image?url=https%3A%2F%2Fdailydressme.com%2Fassets%2F200x%2Cq90%2Fe37a3d2541153dc3f0d7002d283ff94f%2Fa3860b58%2FRowanDress2.jpg&w=3840&q=75'
        'https://dailydressme.com/_next/image?url=https%3A%2F%2Fdailydressme.com%2Fassets%2F200x%2Cq90%2F878b1f2faa3390643a5d25cc5c185f1e%2F03eca1a5%2FFunnelNeckSweaterSplendidbrand-Splendid.jpg&w=3840&q=75'
    ]


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


def json_weather_to_model(weather: dict) -> dict:
    time = weather['dt_txt'].split(' ')[1]
    weather['weather'] = weather['weather'][0]
    weather['time_txt_info'] = time_to_word[time]
    weather['weather']['clothes_list'] = get_clothes_list(temp=0)
    weather['weather']['icon_src'] = get_icon_src(weather['weather']['icon'])
    return weather


def get_weather(json_data: dict) -> WeatherMainAnswer:
    weather_json_list = json_data['list']
    day_weather_now = weather_json_list[1]['dt_txt'].split(' ')[0]
    day_weather_list = [json_weather_to_model(weather_json_list[1])]
    weather_json_list = weather_json_list[2:]
    for weather in weather_json_list:
        spl = weather['dt_txt'].split(' ')
        date = spl[0]
        time = spl[1]
        if day_weather_now == date:
            continue
        if time == '15:00:00':  # day
            day_weather_list.append(json_weather_to_model(weather))
    json_data['list'] = day_weather_list
    return WeatherMainAnswer(**json_data)
