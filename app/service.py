import requests
import os
import logging
from models import WeatherResponse

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY", "9e469a336cc7ed95387acd98babd13b2")
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
        
        # Pastikan data memiliki struktur yang benar
        if all(k in data for k in ("name", "main", "weather", "wind")):
            return WeatherResponse(
                city=data["name"],
                temperature=data["main"].get("temp", 0),  # Gunakan .get untuk menghindari KeyError
                weather=data["weather"][0].get("description", "Unknown"),
                humidity=data["main"].get("humidity", 0),
                wind_speed=data["wind"].get("speed", 0)
            )
        else:
            logger.error(f"Data tidak lengkap untuk kota {city}: {data}")
            return None  # Data tidak valid
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error mengambil data cuaca untuk {city}: {str(e)}")
        return None  # Jika terjadi error
