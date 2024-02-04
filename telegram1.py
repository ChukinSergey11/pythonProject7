import asyncio
from aiogram import Bot,Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token="6914573605:AAGFQUPzhJAo-CikJ3KPqu2YwjOk2GxbRHo")

dp =Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer('Это была команда старт')

@dp.message()
async def start_cmd(message:types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())