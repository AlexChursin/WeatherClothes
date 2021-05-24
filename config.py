import os

from dotenv import load_dotenv

load_dotenv()
API_WEATHER_HOST = os.getenv("API_WEATHER_HOST")
API_KEY = os.getenv("API_KEY")
DATETIME_F = "%Y-%M-%d %H:%M:%S"
