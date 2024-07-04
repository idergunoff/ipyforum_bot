from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from emoji import emojize

cb_photo = CallbackData('Photos', 'page')
cb_calendar = CallbackData('Calendar', 'day')
cb_about = CallbackData('About', 'page')
cb_map = CallbackData('Map', 'page')
cb_link = CallbackData('Link', 'link_id')
cb_answ_quest = CallbackData('Quest', 'quest_id')
cb_add_admin = CallbackData('Admin', 'user_id')
cb_part = CallbackData('Participant', 'name')

btn_about = KeyboardButton(emojize('О форуме :placard:'))
btn_calendar = KeyboardButton(emojize('Программа :tear-off_calendar:'))
btn_map = KeyboardButton(emojize('Схема кампуса :world_map:'))
btn_picture = KeyboardButton(emojize('Фото :camera_with_flash:'))
btn_support = KeyboardButton(emojize('Помощь :red_question_mark:'))
btn_chat = KeyboardButton(emojize('Чат :speech_balloon:'))
btn_sammit = KeyboardButton(emojize('Вопрос на Саммит :globe_with_meridians:'))
btn_location = KeyboardButton(emojize('Место проведения 📍'))
btn_transfer = KeyboardButton(emojize('Заказать трансфер 🚌'))

btn_send_photo = InlineKeyboardButton(emojize('Отправить фото:camera:'), callback_data='send_photo')
btn_add_link = InlineKeyboardButton(emojize('Добавить ссылку'), callback_data='add_link')
btn_del_link = InlineKeyboardButton(emojize('Удалить ссылку'), callback_data='del_link')
btn_ask_quest = InlineKeyboardButton(emojize('Задать вопрос'), callback_data='send_question')
btn_no_answ = InlineKeyboardButton(emojize('Неотвеченные вопросы'), callback_data='no_answered')
btn_cancel = InlineKeyboardButton(emojize('Отмена'), callback_data='cancel')
btn_quest_summit = InlineKeyboardButton('Отправить вопрос на Саммит', callback_data='quest_summit')
btn_get_quests = InlineKeyboardButton('Получить вопросы', callback_data='get_quests')

# btn_1007 = InlineKeyboardButton(emojize('10.07/Вс'), callback_data=cb_calendar.new(day=0))
# btn_1107 = InlineKeyboardButton(emojize('11.07/Пн'), callback_data=cb_calendar.new(day=1))
# btn_1207 = InlineKeyboardButton(emojize('12.07/Вт'), callback_data=cb_calendar.new(day=2))
# btn_1307 = InlineKeyboardButton(emojize('13.07/Ср'), callback_data=cb_calendar.new(day=3))
# btn_1407 = InlineKeyboardButton(emojize('14.07/Чт'), callback_data=cb_calendar.new(day=4))
# btn_1507 = InlineKeyboardButton(emojize('15.07/Пт'), callback_data=cb_calendar.new(day=5))
# btn_1607 = InlineKeyboardButton(emojize('16.07/Сб'), callback_data=cb_calendar.new(day=6))
# btn_1707 = InlineKeyboardButton(emojize('17.07/Вс'), callback_data=cb_calendar.new(day=7))

btn_part_1 = InlineKeyboardButton(emojize('Минниханов Р.Н.'), callback_data=cb_part.new(name='Минниханов Р.Н.'))
btn_part_2 = InlineKeyboardButton(emojize('Сорокин П.Ю.'), callback_data=cb_part.new(name='Сорокин П.Ю.'))
btn_part_3 = InlineKeyboardButton(emojize('Чернышов Б.А.'), callback_data=cb_part.new(name='Чернышов Б.А.'))
btn_part_4 = InlineKeyboardButton(emojize('Маганов Н.У.'), callback_data=cb_part.new(name='Маганов Н.У.'))
btn_part_5 = InlineKeyboardButton(emojize('Крюков В.А.'), callback_data=cb_part.new(name='Крюков В.А.'))
btn_part_6 = InlineKeyboardButton(emojize('Коляденко И.А.'), callback_data=cb_part.new(name='Коляденко И.А.'))


kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb_start.row(btn_about, btn_calendar).row(btn_location, btn_map).row(btn_transfer, btn_picture, btn_support).row(btn_chat, btn_sammit)

# kb_calendar = InlineKeyboardMarkup(row_width=4)
# kb_calendar.insert(btn_1007).insert(btn_1107).insert(btn_1207).insert(btn_1307).insert(btn_1407).insert(btn_1507).\
#     insert(btn_1607).insert(btn_1707)
    
kb_link_photo = InlineKeyboardMarkup(row_width=2)
kb_link_photo.row(btn_add_link, btn_del_link)

kb_ask_quest = InlineKeyboardMarkup(row_width=1)
kb_ask_quest.add(btn_ask_quest)

kb_no_answ = InlineKeyboardMarkup(row_width=1)
kb_no_answ.add(btn_ask_quest).add(btn_no_answ)

kb_summit = InlineKeyboardMarkup(row_width=1)
kb_summit.add(btn_quest_summit)

kb_summit_admin = InlineKeyboardMarkup(row_width=1)
kb_summit_admin.add(btn_quest_summit).add(btn_get_quests)

kb_part = InlineKeyboardMarkup(row_width=1)
kb_part.add(btn_part_1).add(btn_part_2).add(btn_part_3).add(btn_part_4).add(btn_part_5).add(btn_part_6).row(btn_cancel)


class ipyforumStates(StatesGroup):
    SEND_PHOTO = State()
    ADD_LINK = State()
    DESC_LINK = State()
    SEND_QUEST = State()
    SEND_ANSWER = State()
    SUMMIT = State()
