from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from emoji import emojize

cb_photo = CallbackData('Photos', 'page')
cb_calendar = CallbackData('Calendar', 'day')


btn_about = (emojize('О форуме :placard:'))
btn_calendar = KeyboardButton(emojize('Программа :tear-off_calendar:'))
btn_map = KeyboardButton(emojize('Карта :world_map:'))
btn_picture = KeyboardButton(emojize('Галерея :camera_with_flash:'))
btn_support = KeyboardButton(emojize('Помощь :red_question_mark:'))
btn_chat = KeyboardButton(emojize('Чат :speech_balloon:'))

btn_send_photo = InlineKeyboardButton(emojize('Отправить фото:camera:'), callback_data='send_photo')

btn_1007 = InlineKeyboardButton(emojize('10.07/Вс'), callback_data=cb_calendar.new(day=0))
btn_1107 = InlineKeyboardButton(emojize('11.07/Пн'), callback_data=cb_calendar.new(day=1))
btn_1207 = InlineKeyboardButton(emojize('12.07/Вт'), callback_data=cb_calendar.new(day=2))
btn_1307 = InlineKeyboardButton(emojize('13.07/Ср'), callback_data=cb_calendar.new(day=3))
btn_1407 = InlineKeyboardButton(emojize('14.07/Чт'), callback_data=cb_calendar.new(day=4))
btn_1507 = InlineKeyboardButton(emojize('15.07/Пт'), callback_data=cb_calendar.new(day=5))
btn_1607 = InlineKeyboardButton(emojize('16.07/Сб'), callback_data=cb_calendar.new(day=6))
btn_1707 = InlineKeyboardButton(emojize('17.07/Вс'), callback_data=cb_calendar.new(day=7))


kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_start.row(btn_about, btn_calendar).row(btn_map, btn_picture).row(btn_support, btn_chat)

kb_calendar = InlineKeyboardMarkup(row_width=4)
kb_calendar.insert(btn_1007).insert(btn_1107).insert(btn_1207).insert(btn_1307).insert(btn_1407).insert(btn_1507).\
    insert(btn_1607).insert(btn_1707)


class ipyforumStates(StatesGroup):
    SEND_PHOTO = State()
