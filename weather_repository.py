# repositories/weather_repository.py
import os
import json

class WeatherRepository:
    def __init__(self, base_path="data"):
        self.base_path = base_path
        self.categories = ["temperatura", "tiempo", "precipitaciones"]

    def get_data_for_category(self, category):
        path = os.path.join(self.base_path, category, "predictions_ensemble.json")
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_weather_by_date(self, date):
        result = {}
        for category in self.categories:
            data = self.get_data_for_category(category)
            # Filtramos por fecha exacta (YYYY-MM-DD)
            item = next((d for d in data if d["date"].startswith(date)), None)
            result[category] = item
        return result
