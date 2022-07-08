from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Стать пользователем')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button_hi)


parrot_types = ReplyKeyboardMarkup(resize_keyboard=True)
for button in range(1, 5):
    parrot_types.add(KeyboardButton(str(button)))


parrot_params = ReplyKeyboardMarkup(resize_keyboard=True)
for button1 in range(1, 9):
    parrot_params.add(KeyboardButton(str(button1)))

yes_no = ReplyKeyboardMarkup(resize_keyboard=True)
yes_no.row(KeyboardButton('Нет'), KeyboardButton('Да'))


