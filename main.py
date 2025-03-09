# Import FastAPI dari library fastapi
from fastapi import FastAPI

# Membuat instance dari FastAPI
app = FastAPI()

# Menentukan endpoint utama (root) dengan metode GET
@app.get("/")
def read_root():
    """
    Fungsi ini menangani permintaan GET ke endpoint "/".
    Saat diakses, akan mengembalikan pesan selamat datang.
    """
    return {"message": "Welcome to Weather API Tracker DYDY!"}
