import requests
from .config import API_KEY, BASE_URL

def get_weather_data(city: str):
    """
    Fungsi untuk mengambil data cuaca dari OpenWeather API.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Menyediakan suhu dalam Celcius
    }

    try:
        # Mengirim permintaan ke OpenWeather API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Jika terjadi error HTTP, akan men-trigger exception
        
        # Mengambil data dalam format JSON
        data = response.json()

        # Mengembalikan data cuaca yang relevan
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }

    except requests.exceptions.RequestException as e:
        # Jika ada error saat melakukan permintaan API
        raise Exception(f"Error saat mengambil data cuaca: {str(e)}")
    except KeyError:
        # Jika ada data yang tidak ditemukan atau tidak lengkap
        raise Exception("Kota tidak ditemukan atau data tidak lengkap.")
