from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = "YOUR_API_TOKEN"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("🤖 Бот успешно работает!")

if __name__ == "__main__":
    executor.start_polling(dp)
