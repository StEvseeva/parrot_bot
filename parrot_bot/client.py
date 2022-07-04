from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import parrot_bot.keyboards as kb
from parrot_bot.DB import *


TOKEN = "5502102781:AAH73mUH3FPnsvlrGpOKwgxBGbXKXSlpZEE"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    print('/')
    await msg.answer(f'Я бот. Приятно познакомиться, {msg.from_user.first_name}', reply_markup=kb.greet_kb)


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    print('text', msg.text)
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    elif msg.text.lower() == 'стать пользователем':
        add_user(msg.from_user.username, msg.from_user.id)
        await msg.answer('Все готово, теперь можно начинать!')
    else:
        await msg.answer('Не понимаю, что это значит.')


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()


