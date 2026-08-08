from flask import Blueprint, jsonify, request
from core.weather_service import fetch_weather

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/weather/<city>", methods=["GET"])
def get_weather(city):
    result = fetch_weather(city)
    return jsonify(result)
