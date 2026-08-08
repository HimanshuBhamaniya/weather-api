import requests
from config import Config
from core.cache import cache

def fetch_weather(city: str):
    cached = cache.get(city)
    if cached:
        return eval(cached.decode("utf-8"))

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key={Config.WEATHER_API_KEY}&unitGroup=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch data"}

    data = response.json()
    result = {
    "city": city,
    "temperature": data["currentConditions"]["temp"],
    "condition": data["currentConditions"]["conditions"],
    "feelslike": data["currentConditions"]["feelslike"],
    "description": data["description"],  
    "humidity": data["currentConditions"]["humidity"],
    "icon": data["currentConditions"]["icon"]  
}


    cache.setex(city, 43200, str(result))
    return result