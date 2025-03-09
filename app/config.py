import os
from dotenv import load_dotenv

# Memuat file .env ke dalam environment
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY", "9e469a336cc7ed95387acd98babd13b2")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
