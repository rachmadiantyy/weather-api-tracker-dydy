from fastapi import FastAPI
from .routes import router  # Import routes from routes.py
from .config import settings  # Import configuration (API keys, etc.)

app = FastAPI()

# Daftarkan routes
app.include_router(router)

@app.get("/", operation_id="root_get_message")
def read_root():
    """
    Endpoint utama yang mengembalikan pesan selamat datang.
    """
    return {"message": "Welcome to Weather API Tracker DYDY!"}
