FROM python:3.9-slim

WORKDIR /app

# Copy requirements dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file dari folder app ke /app di container
COPY app/ .

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Jalankan uvicorn dengan cara yang benar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]