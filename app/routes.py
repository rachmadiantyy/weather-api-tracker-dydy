# Backup original
cp app/routes.py app/routes.py.backup

# Copy working version
cat > app/routes.py << 'EOF'
from fastapi import APIRouter, HTTPException
import requests
import logging

# Setup logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

# OpenWeatherMap config
API_KEY = "9e469a336cc7ed95387acd98babd13b2"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@router.get("/weather/{city}")
async def get_weather(city: str, units: str = "metric"):
    """
    Get weather data for a specific city
    """
    try:
        logger.info(f"Getting weather for {city}")
        
        # Build URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units={units}"
        
        # Make request to OpenWeatherMap
        response = requests.get(url, timeout=10)
        
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"City '{city}' not found")
        
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Weather service unavailable")
        
        weather_data = response.json()
        
        # Format response
        result = {
            "city": weather_data["name"],
            "country": weather_data["sys"]["country"],
            "temperature": weather_data["main"]["temp"],
            "feels_like": weather_data["main"]["feels_like"],
            "description": weather_data["weather"][0]["description"],
            "humidity": weather_data["main"]["humidity"],
            "pressure": weather_data["main"]["pressure"],
            "units": units,
            "status": "success"
        }
        
        logger.info(f"Weather data retrieved successfully for {city}")
        return result
        
    except requests.exceptions.RequestException as req_error:
        logger.error(f"Request error for {city}: {req_error}")
        raise HTTPException(status_code=500, detail="Failed to fetch weather data")
    
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    
    except Exception as error:
        logger.error(f"Unexpected error for {city}: {error}")
        raise HTTPException(status_code=500, detail="Internal server error")
EOF

# Rebuild container
docker-compose down
docker-compose up --build -d

# Test
curl "http://localhost:8000/weather/Jakarta"