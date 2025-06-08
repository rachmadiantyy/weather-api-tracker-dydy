from fastapi import APIRouter, HTTPException
from services import get_weather_data  # Ubah dari 'service' ke 'services'
from models import WeatherResponse

router = APIRouter()

@router.get("/weather/{city}", response_model=WeatherResponse, operation_id="get_weather_by_city")
def get_weather(city: str):
    """
    Mengambil data cuaca berdasarkan nama kota.
    """
    weather_data = get_weather_data(city)
    
    # Pastikan weather_data tidak None
    if weather_data:
        return weather_data
    # Menangani jika data tidak ditemukan
    raise HTTPException(status_code=404, detail="Kota tidak ditemukan atau data tidak valid")