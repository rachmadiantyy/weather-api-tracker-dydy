#kode yang akan mendefinisikan endpoint
from fastapi import APIRouter, HTTPException
from .weather import get_weather_data

router = APIRouter()

@router.get("/weather/{city}")
def get_weather(city: str):
    """
    Mengambil data cuaca berdasarkan nama kota.
    """
    try:
        weather_data = get_weather_data(city)
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
