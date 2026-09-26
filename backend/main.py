"""Backend FastAPI cho Bài 8: tra cứu thời tiết hiện tại."""

import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException


ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

# TODO 1/5: Đọc OPENWEATHER_API_KEY từ biến môi trường bằng os.getenv().
API_KEY = os.getenv('OPENWEATHER_API_KEY')
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

app = FastAPI(title="Bài 8 - Weather API")


def get_weather(city: str):
    """Gọi OpenWeatherMap và đổi JSON lớn thành dữ liệu app cần dùng."""
    # TODO 2/5: Tạo dict params gồm q, appid, units="metric" và lang="vi".
    params = {'q': city,
    'appid' : API_KEY,
    'units' : 'metric',
    'lang' : 'vi' }

    # TODO 3/5: Gửi GET request đến WEATHER_URL, truyền params và timeout=10.
    response = requests.get(WEATHER_URL,params=params,timeout=10)

    if response is None or response.status_code != 200:
        return None

    data = response.json()
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
    }


@app.get("/")
def home():
    return {"message": "Weather API đang chạy"}


@app.get("/weather")
def weather(city: str):
    # TODO 4/5: Gọi get_weather(city) và lưu kết quả vào biến data.
    data = get_weather(city)
    if data is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy thành phố")
    return data

