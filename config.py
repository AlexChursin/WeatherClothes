import os

from dotenv import load_dotenv

load_dotenv()
API_WEATHER_HOST = os.getenv("API_WEATHER_HOST")
API_ADMIN_HOST = os.getenv("API_ADMIN_HOST")
API_KEY = os.getenv("API_KEY")
DATETIME_F = "%Y-%m-%d %H:%M:%S"
