from config import *
from button import *
from func import *


t10 = emojize('<u><b>Программа 10 июля</b> (Понедельник)</u>\n\n:alarm_clock:<u><b>9:00 - 22:00</b></u>'
              '\n:smiling_face_with_open_hands:Заезд участников'
    # '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
    # '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
    '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин')
t11 = emojize('<u><b>Программа 11 июля</b> (Вторник)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
              '\n\n:alarm_clock:<u><b>9:00 - 10:00</b></u>Тренинг\n:bust_in_silhouette:для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nЭкскурсия\n:bust_in_silhouette:для тех, кто заехал 10 июля'
              '\n\n:alarm_clock:<u><b>10:30 - 11:00</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:00 - 12:30</b></u>Тренинг\n:bust_in_silhouette:для преподавателей \n:pushpin:Зал "Первомайский"'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nЭкскурсия\n:bust_in_silhouette:для тех, кто заехал 10 июля'
              '\n\n:alarm_clock:<u><b>12:30 - 13:30</b></u>\n:pot_of_food:Обед'
              '\n\n:alarm_clock:<u><b>14:00 - 16:00</b></u>\nТренинг «Командообразование», веревочный курс, Корп. Университет'
              '\n:bust_in_silhouette:Группа А'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nТренинг "Дизайн мышление", Корп. Университет\n:bust_in_silhouette: Группа Б\n:pushpin: Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>16:00 - 16:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:30 - 19:00</b></u>'
              '\nТренинг "Дизайн мышление", Корп. Университет\n:bust_in_silhouette: Группа А\n:pushpin: Большой зал "Ромашкино"'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nТренинг «Командообразование», веревочный курс, Корп. Университет'
              '\n:bust_in_silhouette:Группа Б'
              '\n\n:alarm_clock:<u><b>18:30 - 19:30</b></u>\n:pot_of_food:Ужин'
              '\n\n:alarm_clock:<u><b>19:30 - 20:00</b></u>\n:FREE_button:Свободное время'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nТОРЖЕСТВЕННОЕ ОТКРЫТИЕ  4-го Международного нефтегазового '
              'молодежного форума \n:pushpin:Футбольное поле')

t12 = emojize('<u><b>Программа 12 июля</b> (Среда)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nТренинг "Бизнес-моделирование"\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nТРЕНИНГ «ТрендЛаб»\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
              '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nОТКРЫТЫЙ ЛЕКТОРИЙ\n:pushpin:Большой зал "Ромашкино"\nЭкспертная гостинная'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nУСТАНОВОЧНЫЙ семинар\n:bust_in_silhouette:с экспертами хакатона\n:pushpin:Зал Ново-Елховский'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nФорсайт сессия\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин'
              '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nУстановочный тренинг на работу с кейсом\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nКультурно-развлекательная программа\nИнтеллектуальная игра'
              '\n:pushpin:Большой зал "Ромашкино"')

t13 = emojize('<u><b>Программа 13 июля</b> (Четверг)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nТренинг "Креативная уверенность"\n:bust_in_silhouette:Группа А\n:pushpin:Футбольное поле'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nЖеребьевка Хакатона. Представление экспертов. '
              'Представление заданий и проведение жеребьевки среди команд.\n:pushpin:Футбольное поле'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
              '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nХакатон Развития ТЭК 2023: Начало работы команд'
              '\n:pushpin:2-а зала, два шатра по направлениям, в каждом помещении минимум по 3 эксперта '
              '(эксперты могут меняться в течение 2-х часов по запросам команд)'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nХакатон Развития ТЭК 2023: Продолжение работы команд'
              '\n:pushpin:2-а зала, два шатра по направлениям, в каждом помещении минимум по 3 эксперта '
              '(эксперты могут меняться в течение 2-х часов по запросам команд)'
              '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин'
              '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nЭкспертная гостинная:\n:pushpin: зал "Архангельский"'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nКультурно-развлекательная программа\n:pushpin:Футбольное поле')

t14 = emojize('<u><b>Программа 14 июля</b> (Пятница)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nНЕФТЯНОЙ САММИТ Республики Татарстан\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nНЕФТЯНОЙ САММИТ Республики Татарстан\nДиалог на равных\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
              '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nХакатон Развития ТЭК 2022: Продолжение работы команд\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nХакатон Развития ТЭК 2023: Продолжение работы команд\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин'
              '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nТренинг "Успешная презентация перед инвестором"\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nЭкспертная гостиная\n:pushpin:Большой зал "Ромашкино"')

t15 = emojize('<u><b>Программа 15 июля</b> (Суббота)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nХакатон Развития ТЭК 2023: Продолжение работы команд\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nХакатон Развития ТЭК 2023: Продолжение работы команд\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
              '\n\n:alarm_clock:<u><b>14:00 - 14:30</b></u>\nПроведение жеребьёвки выступлений команд на предзащите\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>14:30 - 15:30</b></u>\nПРЕДЗАЩИТА ПРОЕКТНЫХ РЕШЕНИЙ (по 4-м направлениям)\n'
              ':pushpin:4 зала (Ромашкино, Ново-Елховский, Бондюжский, Архангельский)'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nПРЕДЗАЩИТА ПРОЕКТНЫХ РЕШЕНИЙ (по 4-м направлениям)\n'
              ':pushpin:4 зала (Ромашкино, Ново-Елховский, Бондюжский, Архангельский)'
              '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин'
              '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nОБЪЯВЛЕНИЕ ФИНАЛИСТОВ.\nПроведение жеребьёвки выступлений '
              'на финальной защите\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nСвободное время.\nКоманды-финалисты готовятся к финальное защите проектов')

t16 = emojize('<u><b>Программа 16 июля</b> (Воскресенье)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nФИНАЛ: ЗАЩИТА ПРОЕКТОВ\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nФИНАЛ: ЗАЩИТА ПРОЕКТОВ\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
              '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nПОДВЕДЕНИЕ ИТОГОВ\nСовещание соревновательного жюри.'
              '\nОбработка результатов голосования.\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение со старожилом форума Мистером Эчпочмаком'
              '\n\n:alarm_clock:<u><b>16:00 - 17:00</b></u>\n:FREE_button:Свободное время'
              '\n\n:alarm_clock:<u><b>17:00 - 18:00</b></u>\nОФИЦИАЛЬНОЕ ЗАКРЫТИЕ ФОРУМА.\nОБЪЯВЛЕНИЕ ПОБЕДИТЕЛЕЙ\n:pushpin:Большой зал "Ромашкино"'
              '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин'
              '\n\n:alarm_clock:<u><b>19:00 - 22:00</b></u>\nКультурная программа')
t17 = emojize('<u><b>Программа 17 июля</b> (Понедельник)</u>'
              '\n\n:alarm_clock:<u><b>9:00 - 22:00</b></u>\n:airplane_departure:Отъезд участников')

list_calendar = [t10, t11, t12, t13, t14, t15, t16, t17]
list_button = ['10.07/Пн', '11.07/Вт', '12.07/Ср', '13.07/Чт', '14.07/Пт', '15.07/Сб', '16.07/Вс', '17.07/Пн']


@dp.message_handler(text=emojize('Программа :tear-off_calendar:'))
async def calendar(msg: types.Message):
    day = datetime.datetime.now().strftime('%d')
    if 0 <= int(day) - 10 <= 8:
        mes = list_calendar[int(day) - 10]
    else:
        mes = list_calendar[0]
    kb_calendar = InlineKeyboardMarkup(row_width=3)
    for i in range(8):
        if i == int(day) - 10:
            kb_calendar.insert(InlineKeyboardButton(f'- {list_button[i]} -', callback_data='no'))
        else:
            kb_calendar.insert(InlineKeyboardButton(list_button[i], callback_data=cb_calendar.new(day=i)))
    await send_message_try(msg.from_user.id, mes, kb_calendar)


@dp.callback_query_handler(cb_calendar.filter())
async def calendar_day(call: types.CallbackQuery, callback_data: dict):
    mes = list_calendar[int(callback_data['day'])]
    kb_calendar = InlineKeyboardMarkup(row_width=3)
    for i in range(8):
        if i == int(callback_data['day']):
            kb_calendar.insert(InlineKeyboardButton(f'- {list_button[i]} -', callback_data='no'))
        else:
            kb_calendar.insert(InlineKeyboardButton(list_button[i], callback_data=cb_calendar.new(day=i)))
    try:
        await call.message.edit_text(mes, reply_markup=kb_calendar)
    except exceptions.MessageNotModified:
        pass
    await call.answer()


@dp.callback_query_handler(text='no')
async def no(call: types.CallbackQuery):
    await call.answer()