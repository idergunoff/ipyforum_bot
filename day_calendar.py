from config import *
from button import *
from func import *


t10 = emojize('<u><b>Программа 10 июля</b></u>\n\n:alarm_clock:<u><b>9:00 - 22:00</b></u>\nЗаезд участников')
t11 = emojize('<u><b>Программа 11 июля</b></u>'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nТренинг для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:counterclockwise_arrows_button::counterclockwise_arrows_button::counterclockwise_arrows_button:'
              '\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\nОбед'
              '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nТренинг для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:counterclockwise_arrows_button::counterclockwise_arrows_button::counterclockwise_arrows_button:'
              '\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nТренинг "СОБИРАЕМ КОМАНДУ ДЛЯ СТАРТАПА С "о" \n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\nСвободное время'
              '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nУжин'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nТОРЖЕСТВЕННОЕ ОТКРЫТИЕ 3-го Международного нефтегазового '
              'молодежного форума \n:pushpin:Футбольное поле')
t12 = emojize('<u><b>Программа 12 июля</b></u>'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nНЕФТЯНОЙ САММИТ Республики Татарстан\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nНЕФТЯНОЙ САММИТ Республики Татарстан\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\nОбед'
              '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nОТКРЫТЫЙ ЛЕКТОРИЙ (Вводные лекции по направлениям Хакатона)\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:00 - 19:00</b></u>\nТренинг "ЭФФЕКТИВНАЯ РАБОТА В КОМАНДЕ" \n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nУжин'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nЖЕРЕБЬЕВКА ХАКАТОНА. Представление экспертов. '
              'Представление заданий и проведение жеребьевки среди команд\n:pushpin:Большой зал "Ромашкино"')
t13 = emojize('<u><b>Программа 13 июля</b></u>'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nТренинг для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:counterclockwise_arrows_button:\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\nОбед'
              '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nТренинг для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:counterclockwise_arrows_button:\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nТренинг "СОБИРАЕМ КОМАНДУ ДЛЯ СТАРТАПА С "о" \n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\nСвободное время'
              '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nУжин'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nТОРЖЕСТВЕННОЕ ОТКРЫТИЕ 3-го Международного нефтегазового '
              'молодежного форума \n:pushpin:Футбольное поле')
t14 = emojize('<u><b>Программа 14 июля</b></u>'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nТренинг для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:counterclockwise_arrows_button:\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\nОбед'
              '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nТренинг для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:counterclockwise_arrows_button:\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nТренинг "СОБИРАЕМ КОМАНДУ ДЛЯ СТАРТАПА С "о" \n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\nСвободное время'
              '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nУжин'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nТОРЖЕСТВЕННОЕ ОТКРЫТИЕ 3-го Международного нефтегазового '
              'молодежного форума \n:pushpin:Футбольное поле')
t15 = emojize('<u><b>Программа 15 июля</b></u>'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nТренинг для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:counterclockwise_arrows_button:\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\nОбед'
              '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nТренинг для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:counterclockwise_arrows_button:\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nТренинг "СОБИРАЕМ КОМАНДУ ДЛЯ СТАРТАПА С "о" \n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\nСвободное время'
              '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nУжин'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nТОРЖЕСТВЕННОЕ ОТКРЫТИЕ 3-го Международного нефтегазового '
              'молодежного форума \n:pushpin:Футбольное поле')
t16 = emojize('<u><b>Программа 16 июля</b></u>'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nТренинг для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:counterclockwise_arrows_button:\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\nОбед'
              '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nТренинг для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:counterclockwise_arrows_button:\nЭкскурсия для студентов и молодых специалистов'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\nВкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nТренинг "СОБИРАЕМ КОМАНДУ ДЛЯ СТАРТАПА С "о" \n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\nСвободное время'
              '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nУжин'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nТОРЖЕСТВЕННОЕ ОТКРЫТИЕ 3-го Международного нефтегазового '
              'молодежного форума \n:pushpin:Футбольное поле')
t17 = emojize('<u><b>Программа 17 июля</b></u>'
              '\n\n:alarm_clock:<u><b>9:00 - 22:00</b></u>\nОтъезд участников')

list_calendar = [t10, t11, t12, t13, t14, t15, t16, t17]


@dp.message_handler(text=emojize('Программа :tear-off_calendar:'))
async def calendar(msg: types.Message):
    day = datetime.datetime.now().strftime('%d')
    if 0 <= int(day) - 10 <= 8:
        mes = list_calendar[int(day) - 10]
    else:
        mes = list_calendar[0]
    await bot.send_message(msg.from_user.id, mes, reply_markup=kb_calendar)


@dp.callback_query_handler(cb_calendar.filter())
async def calendar_day(call: types.CallbackQuery, callback_data: dict):
    mes = list_calendar[int(callback_data['day'])]
    await call.message.edit_text(mes, reply_markup=kb_calendar)
    await call.answer()