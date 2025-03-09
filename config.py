import os
from dotenv import load_dotenv

# Memuat file .env ke dalam environment
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY", "a82c2af37ad2faf45c49462cb034994e")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
