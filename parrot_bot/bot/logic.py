from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from parrot_bot.bot.keyboards import *


class ChooseParrot(StatesGroup):
    waiting_for_parrot_param = State()
    waiting_for_accept = State()


async def choose_parrot_type(message: types.Message):
    await message.answer("Выберите тип попугая:", reply_markup=parrot_types)
    await ChooseParrot.waiting_for_parrot_param.set()


async def choose_parrot_param(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_parrot_types:
        await message.answer("Пожалуйста, выберите тип попугая, используя клавиатуру ниже.")
        return
    await state.update_data(chosen_type=message.text.lower())

    # Для последовательных шагов можно не указывать название состояния, обходясь next()
    await ChooseParrot.next()
    await message.answer("Теперь выберите параметры:", reply_markup=parrot_params)


async def accept_choice(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_parrot_params:
        await message.answer("Пожалуйста, выберите параметры, используя клавиатуру ниже.")
        return
    user_data = await state.get_data()
    await message.answer(f"Вы выбрали попугая №{user_data['chosen_type']} с набором параметров №{message.text.lower()}."
                         "\nВсе верно?",
                         reply_markup=yes_no)
    await state.finish()


def run_life_cycle():
    return


def register_handlers_parrot(disp: Dispatcher):
    disp.register_message_handler(choose_parrot_type, commands="parrot", state="*")
    disp.register_message_handler(choose_parrot_param, state=ChooseParrot.waiting_for_parrot_param)
    disp.register_message_handler(accept_choice, state=ChooseParrot.waiting_for_accept)


available_parrot_types = [str(i) for i in range(1, 5)]
available_parrot_params = [str(i) for i in range(1, 9)]
