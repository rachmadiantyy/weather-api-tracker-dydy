from fastapi import FastAPI
from routes import router  # Import routes from routes.py
from prometheus_fastapi_instrumentator import Instrumentator
from config import API_KEY, BASE_URL
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Weather API Tracker DYDY",
    description="API untuk tracking dan monitoring cuaca",
    version="1.0.0"
)

# Tambahkan middleware Prometheus untuk monitoring
Instrumentator().instrument(app).expose(app)

# Daftarkan routes
app.include_router(router)

@app.get("/", operation_id="root_get_message")
def read_root():
    """
    Endpoint utama yang mengembalikan pesan selamat datang.
    """
    return {"message": "Welcome to Weather API Tracker DYDY!"}

@app.get("/health")
def health_check():
    """
    Health check endpoint untuk monitoring.
    """
    return {
        "status": "healthy",
        "service": "Weather API Tracker DYDY",
        "api_key_configured": bool(API_KEY),
        "base_url": BASE_URL
    }

# Startup event
@app.on_event("startup")
async def startup_event():
    logger.info("Weather API Tracker DYDY started successfully")
    logger.info(f"API Key configured: {'Yes' if API_KEY else 'No'}")
    logger.info(f"Base URL: {BASE_URL}")