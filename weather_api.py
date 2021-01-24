import requests


class OpenWeather:

    def get(self, city):
        api_key = '' # Указываем ключ выданный при регистрации
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&APPID={api_key}&units=metric'
        data = requests.get(url).json()

        if data['cod'] == '404':
            return {'Ошибка': 'Город не найден'}
        else:
            forecast_data = data['main']
            forecast = {
                'Температура (С)': forecast_data['temp'],
                'Ощущается как (С)': forecast_data['feels_like'],
                'Влажность (%)': forecast_data['humidity'],
                'Атмосферное давление': forecast_data['pressure'],
                'Максимальная температура (С)': forecast_data['temp_max'],
                'Минимальная температура (С)': forecast_data['temp_min'],
                'Скорость ветра (м/с)': data['wind']['speed']
            }
            return forecast


class CityInfo:

    def __init__(self, city, forecast_provider=None):
        self.city = city
        self._forecast_provider = forecast_provider or OpenWeather()

    def weather_forecast(self):
        return self._forecast_provider.get(self.city)


def main():

    city_name = input("Введите название города: ")
    city_info = CityInfo(city_name)
    forecast = city_info.weather_forecast()
    for key in forecast:
        print(f'{key}: {forecast[key]}')


if __name__ == "__main__":
    main()
