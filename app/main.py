from fastapi import FastAPI, HTTPException #biar kalo ada error responnya rapi#
from .weather import get_weather_data  # Mengimpor fungsi get_weather_data
from .routes import router

import requests
import os


app = FastAPI()

# Daftarkan routes
app.include_router(router)

# Menggunakan environment variable untuk API key (lebih aman)
API_KEY = os.getenv("OPENWEATHER_API_KEY", "d41e85c52a44f59f36b051b3fdb663d5")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/", operation_id="root_get_message") #operation id agar tidak duplikat pada endpoint
def read_root():
    """
    Endpoint utama yang mengembalikan pesan selamat datang.
    """
    return {"message": "Welcome to Weather API Tracker DYDY!"}

@app.get("/weather/{city}")
def get_weather(city: str):
    """
    Mengambil data cuaca berdasarkan nama kota.
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
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error mengambil data cuaca: {str(e)}")
    except KeyError:
        raise HTTPException(status_code=404, detail="Kota tidak ditemukan atau data tidak lengkap")
