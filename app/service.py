import requests
import os
import logging
import traceback  # TAMBAHKAN INI
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
        "units": "metric"
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if all(k in data for k in ("name", "main", "weather", "wind")):
            return WeatherResponse(
                city=data["name"],
                temperature=data["main"].get("temp", 0),
                weather=data["weather"][0].get("description", "Unknown"),
                humidity=data["main"].get("humidity", 0),
                wind_speed=data["wind"].get("speed", 0)
            )
        else:
            logger.error(f"Data tidak lengkap untuk kota {city}: {data}")
            return None
        
    except Exception as exc:  # UBAH DARI 'e' KE 'exc'
        logger.error(f"Full traceback:")
        traceback.print_exc()  # TAMBAHKAN INI
        logger.error(f"Error mengambil data cuaca untuk {city}: {str(exc)}")
        return None