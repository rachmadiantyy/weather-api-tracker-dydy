# Gunakan image Python
FROM python:3.9

# Set working directory di dalam container
WORKDIR /app

# Copy file requirements.txt ke dalam container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh file aplikasi ke dalam container
COPY . /app/

# Jalankan aplikasi dengan uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
