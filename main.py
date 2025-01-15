import asyncio
import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

# Вставьте ваш API ключ и название города
WEATHER_API_KEY = '69b5affaf4e6cba93bc238ab505eaa0e'
CITY_NAME = 'Moscow'

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={WEATHER_API_KEY}&units=metric&lang=ru'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        return f"Текущая температура в {CITY_NAME}: {temperature}°C"
    else:
        return "Не удалось получить данные о погоде."

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help\n/weather")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, я бот!")

@dp.message(Command('weather'))
async def weather(message: Message):
    weather_info = get_weather()
    await message.answer(weather_info)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



