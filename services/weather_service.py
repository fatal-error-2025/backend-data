# services/weather_service.py
class WeatherService:
    def __init__(self, repository):
        self.repository = repository

    def get_weather_by_date(self, date):
        return self.repository.get_weather_by_date(date)
