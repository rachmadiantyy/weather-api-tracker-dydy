# weather-api-tracker-dydy
# PUNYA DIANTY
🚀 Features
✅ Fetch current weather by city name
✅ Supports OpenWeatherMap API (or any other API you choose)
✅ Exposes Swagger UI for API documentation (/docs)
✅ CI/CD with Jenkins
✅ Integrated with Prometheus & New Relic for monitoring

📂 Project Structure
plaintext
Copy
Edit
weather-api-tracker/
│── app/
│   ├── main.py            # FastAPI main application
│   ├── config.py          # API configurations
│   ├── services.py        # Weather fetching logic
│   ├── models.py          # Data models
│   ├── routes.py          # API routes
│── tests/                 # Unit tests
│── .gitignore             # Ignore unnecessary files
│── Dockerfile             # Containerize the app
│── docker-compose.yml     # Docker setup for multi-services
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
│── jenkinsfile            # CI/CD pipeline
⚡ Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/username/weather-api-tracker.git
cd weather-api-tracker
Create Virtual Environment & Install Dependencies

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Run the Application

bash
Copy
Edit
uvicorn app.main:app --reload
Access Swagger UI

Open http://127.0.0.1:8000/docs in the browser.
📊 Monitoring with New Relic
Sign up & get New Relic API key.
Install newrelic Python agent.
bash
Copy
Edit
pip install newrelic
Run the app with New Relic monitoring.
bash
Copy
Edit
newrelic-admin run-program uvicorn app.main:app --reload