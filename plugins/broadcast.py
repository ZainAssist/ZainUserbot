from telethon import events
import requests

@events.register(events.NewMessage(pattern=".weather"))
async def weather_handler(event):
    city = event.text.split()[1]
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    weather = response["weather"][0]["description"]
    await event.reply(f"Weather in {city}: {weather} 🌤️")
