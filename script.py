import requests
from rich.console import Console
from rich.table import Table
from rich import box

API_KEY = '7019e61a0defc22ac9d5f8c07a896d1f'  # Your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def display_weather(data):
    console = Console()
    
    if data.get('cod') != 200:
        console.print(f"[bold red]Error: {data.get('message', 'Unable to fetch weather data')}[/bold red]")
        return

    city = data['name']
    weather_desc = data['weather'][0]['description'].title()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    table = Table(title=f"Weather in {city}", box=box.DOUBLE_EDGE, style="blue")

    table.add_column("Description", justify="left")
    table.add_column("Temperature (°C)", justify="right")
    table.add_column("Feels Like (°C)", justify="right")
    table.add_column("Humidity (%)", justify="right")
    table.add_column("Wind Speed (m/s)", justify="right")

    table.add_row(
        weather_desc,
        f"{temp} °C",
        f"{feels_like} °C",
        f"{humidity} %",
        f"{wind_speed} m/s"
    )

    console.print(table)

if __name__ == "__main__":
    console = Console()
    city = console.input("[bold blue]Enter city name:[/bold blue] ")
    weather_data = get_weather(city)
    display_weather(weather_data)
