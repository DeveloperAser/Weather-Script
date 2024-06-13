#Developer Aser
#Import requirments 
import requests
from rich.console import Console
from rich.table import Table
from rich import box

API_KEY = '7019e61a0defc22ac9d5f8c07a896d1f'  # OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather' #OpenWeatherMap Website

# List of cities I know!
CITIES = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
    "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington"
]

# Using API key we get weather
def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# We print it in a Table format because that is beautiful (I don't know UI very much)
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

# Choose from the list of cities
def choose_city():
    console = Console()
    table = Table(title="Choose a City", box=box.SQUARE)

    table.add_column("Number", justify="right", style="cyan", no_wrap=True)
    table.add_column("City", style="magenta")

    for idx, city in enumerate(CITIES, start=1):
        table.add_row(str(idx), city)

    console.print(table)
    while True:
        choice = console.input("[bold blue]Enter the number of the city:[/bold blue] ")
        if choice.isdigit() and 1 <= int(choice) <= len(CITIES):
            return CITIES[int(choice) - 1]
        else:
            console.print("[bold red]Invalid choice, please enter a valid number.[/bold red]")

# START
if __name__ == "__main__":
    city = choose_city()
    weather_data = get_weather(city)
    display_weather(weather_data)
