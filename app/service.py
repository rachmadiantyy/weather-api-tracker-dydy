import requests
import os
from .models import WeatherResponse

API_KEY = os.getenv("OPENWEATHER_API_KEY","a82c2af37ad2faf45c49462cb034994e")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city: str) -> WeatherResponse:
    """
    Mengambil data cuaca dari OpenWeatherMap API berdasarkan nama kota.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Satuan Celcius
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Jika HTTP error, langsung raise exception
        
        data = response.json()
        
        # Mengembalikan data cuaca yang diperlukan
        return WeatherResponse(
            city=data["name"],
            temperature=data["main"]["temp"],
            weather=data["weather"][0]["description"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"]
        )
    
    except requests.exceptions.RequestException as e:
        return None  # Kembalikan None jika terjadi error
