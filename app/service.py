def get_weather_data(city: str) -> WeatherResponse:
    """
    Mengambil data cuaca dari OpenWeatherMap API berdasarkan nama kota.
    """
    logger.info(f"Getting weather data for city: {city}")
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    try:
        logger.info(f"Making request to {BASE_URL} with params: {params}")
        response = requests.get(BASE_URL, params=params)
        logger.info(f"Response status: {response.status_code}")
        
        response.raise_for_status()
        data = response.json()
        logger.info(f"Response data keys: {data.keys()}")
        
        # Pastikan data memiliki struktur yang benar
        if all(k in data for k in ("name", "main", "weather", "wind")):
            logger.info("Creating WeatherResponse object")
            weather_response = WeatherResponse(
                city=data["name"],
                temperature=data["main"].get("temp", 0),
                weather=data["weather"][0].get("description", "Unknown"),
                humidity=data["main"].get("humidity", 0),
                wind_speed=data["wind"].get("speed", 0)
            )
            logger.info("WeatherResponse created successfully")
            return weather_response
        else:
            logger.error(f"Data tidak lengkap untuk kota {city}: {data}")
            return None
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error untuk {city}: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error untuk {city}: {str(e)}")
        return None