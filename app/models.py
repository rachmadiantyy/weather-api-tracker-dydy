#***************************************************************************#
# models.py yang berisi struktur data untuk response API kamu
# Dianty 
#***************************************************************************
from pydantic import BaseModel

class WeatherResponse(BaseModel): #kelas yang mewakili data yang akan dikembalikan oleh API cuaca.
    city: str
    temperature: float
    weather: str
    humidity: int
    wind_speed: float
