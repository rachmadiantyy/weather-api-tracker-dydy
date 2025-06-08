from fastapi import FastAPI
from routes import router  # Import routes from routes.py
from prometheus_fastapi_instrumentator import Instrumentator  # Tambahkan ini
from config import API_KEY, BASE_URL  # Sesuaikan import sesuai kebutuhan

app = FastAPI()
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
