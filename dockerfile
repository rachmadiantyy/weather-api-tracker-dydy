FROM python:3.9-slim

WORKDIR /app

# Copy requirements dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file aplikasi
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Run the Python script directly instead of uvicorn
CMD ["python", "main.py"]