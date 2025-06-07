from fastapi import APIRouter, HTTPException
from service import get_weather_data
from .models import WeatherResponse


router = APIRouter()

@router.get("/weather/{city}", response_model=WeatherResponse, operation_id="get_weather_by_city")
def get_weather(city: str):
    """
    Mengambil data cuaca berdasarkan nama kota.
    """
    weather_data = get_weather_data(city)
    if weather_data:
        return weather_data
    raise HTTPException(status_code=404, detail="Kota tidak ditemukan")
