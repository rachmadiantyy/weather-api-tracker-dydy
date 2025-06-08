#!/usr/bin/env python3

import sys
import os
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("=== Starting Weather API Tracker DYDY ===")
        logger.info(f"Python version: {sys.version}")
        logger.info(f"Current working directory: {os.getcwd()}")
        logger.info(f"Files in current directory: {os.listdir('.')}")
        
        # Add current directory to path
        current_dir = Path(__file__).parent.absolute()
        if str(current_dir) not in sys.path:
            sys.path.insert(0, str(current_dir))
        logger.info(f"Python path: {sys.path[:3]}")
        
        # Import FastAPI
        from fastapi import FastAPI, HTTPException
        from fastapi.responses import JSONResponse
        logger.info("✓ FastAPI imported successfully")
        
        # Try to import Prometheus
        try:
            from prometheus_fastapi_instrumentator import Instrumentator
            logger.info("✓ Prometheus imported successfully")
        except ImportError as e:
            logger.warning(f"⚠ Prometheus not available: {e}")
            Instrumentator = None
        
        # Try to import config
        try:
            from config import API_KEY, BASE_URL
            logger.info("✓ Config imported successfully")
        except ImportError as e:
            logger.warning(f"⚠ Config import failed: {e}")
            API_KEY = "9e469a336cc7ed95387acd98babd13b2"
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
        
        # Create FastAPI app
        app = FastAPI(
            title="Weather API Tracker DYDY",
            description="API untuk tracking dan monitoring cuaca",
            version="1.0.0"
        )
        logger.info("✓ FastAPI app created")
        
        # Add Prometheus if available
        if Instrumentator:
            try:
                Instrumentator().instrument(app).expose(app)
                logger.info("✓ Prometheus monitoring added")
            except Exception as e:
                logger.warning(f"⚠ Prometheus setup failed: {e}")
        
        # Try to import routes
        try:
            from routes import router
            app.include_router(router)
            logger.info("✓ Routes imported and registered")
        except ImportError as e:
            logger.warning(f"⚠ Routes import failed: {e}")
            
            # Fallback route
            @app.get("/weather/{city}")
            async def fallback_weather(city: str):
                return {
                    "error": "Routes module not available",
                    "city": city,
                    "message": f"Import error: {str(e)}"
                }
        
        # Basic routes
        @app.get("/")
        async def read_root():
            return {
                "message": "Welcome to Weather API Tracker DYDY!",
                "status": "running",
                "version": "1.0.0"
            }
        
        @app.get("/health")
        async def health_check():
            return {
                "status": "healthy",
                "service": "Weather API Tracker DYDY",
                "api_key_configured": bool(API_KEY)
            }
        
        @app.exception_handler(Exception)
        async def global_exception_handler(request, exc):
            logger.error(f"Global exception: {exc}", exc_info=True)
            return JSONResponse(
                status_code=500,
                content={"detail": f"Internal server error: {str(exc)}"}
            )
        
        # Start the server
        import uvicorn
        logger.info("🚀 Starting uvicorn server...")
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8000,
            log_level="info"
        )
        
    except Exception as e:
        logger.error(f"❌ Critical startup error: {e}", exc_info=True)
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)