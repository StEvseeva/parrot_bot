from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

import parrot_bot.bot.keyboards as kb
from parrot_bot.bot.logic import *
from parrot_bot.DB import *


async def send_welcome(msg: types.Message):
    print('/')
    await msg.answer(f'Я бот. Приятно познакомиться, {msg.from_user.first_name}', reply_markup=kb.greet_kb)


async def register(msg: types.Message):
    add_user(msg.from_user.username, msg.from_user.id)
    await msg.answer('Все готово, теперь можно начинать!')


async def get_text_messages(msg: types.Message):
    print('text', msg.text)
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    elif msg.text.lower() == 'стать пользователем':
        add_user(msg.from_user.username, msg.from_user.id)
        await msg.answer('Все готово, теперь можно начинать!')
    else:
        await msg.answer('Не понимаю, что это значит.')


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=["start", "help"], state="*")
    dp.register_message_handler(register, commands="register", state="*")
    # dp.register_message_handler(get_text_messages, content_types=['text'], state="*")
    # dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    # dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")


