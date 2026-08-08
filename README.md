# 🌦 Weather API Wrapper Service

A simple, modular **Weather API web app** built with Python (Flask).  
It fetches live weather data from [Visual Crossing](https://www.visualcrossing.com/) and exposes it through a clean API and minimal web UI.  
Includes caching (Redis), rate limiting, and error handling for production‑ready performance.
This project is inspired by the [roadmap.sh Weather API project](https://roadmap.sh/projects/weather-api-wrapper-service)

---

## 📂 Project Structure

```text
weather-api/
│
├── app.py                # Entry point (Flask app)
├── config.py             # Configuration (API keys, secrets)
├── requirements.txt      # Dependencies
├── .env                  # Environment variables
│
├── core/                 # Core business logic
│   ├── weather_service.py
│   ├── cache.py
│   └── rate_limiter.py
│
├── routes/               # API endpoints
│   └── weather_routes.py
│
├── utils/                # Helpers
│   └── error_handler.py
│
├── templates/            # Web UI
    └── index.html

```
---

## ⚙️ Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/weather-api.git
cd weather-api
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate   # Windows (CMD/Git Bash)
source venv/bin/activate # Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```code
WEATHER_API_KEY=your_visualcrossing_api_key
REDIS_URL=redis://localhost:6379/0
```
5. **Run Redis locally**

. Windows: install Redis or use WSL/Docker

. Linux/Mac: redis-server

6. **Start the app**
```bash
python app.py
```
---

## 🌐 API Endpoints
#### Get weather by city

```Code
GET /weather/<city>
```
**Example:**
```Code
/weather/Delhi
```
**Sample JSON Response**
```text
json
{
  "city": "Delhi,IN",
  "temperature": 31.6,
  "feelslike": 33.0,
  "condition": "Partially cloudy",
  "description": "Warm day with scattered clouds",
  "humidity": 65,
  "icon": "partly-cloudy-day"
}
```

---
## 🎨 Web UI
. Minimal HTML form (index.html) to enter a city name.

. Displays: City, Temperature, Feels like, Humidity, Condition, Description.
**Example**
```text
Bangalore,IN
Temperature: 27.9°C
Feels Like: 30.5°C
Humidity: 70%
Condition: Partially cloudy
Description: Similar temperatures continuing with a chance of rain multiple days.
```

---
## 🛡 Features
. Caching: Redis stores results for 12 hours.

. Rate Limiting: Prevents abuse (100 requests/hour).

. Error Handling: Consistent JSON error responses.

. Extensible: Easy to add more fields (wind speed, pressure, etc.).