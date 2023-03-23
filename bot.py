from aiogram import Bot, Dispatcher, executor
import logging

TOKEN = ''

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
DP = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
