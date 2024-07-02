from config import *
from button import *
from func import *


# t10 = emojize('<u><b>Программа 10 июля</b> (Понедельник)</u>\n\n:alarm_clock:<u><b>9:00 - 22:00</b></u>'
#               '\n:smiling_face_with_open_hands:Заезд участников'
#     # '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
#     '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
#     '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин')
# t11 = emojize('<u><b>Программа 11 июля</b> (Вторник)</u>'
#               '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка "Dance mix"'
#               '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
#               '\n\n:alarm_clock:<u><b>9:00 - 10:00</b></u>\nТренинг\n:bust_in_silhouette:для преподавателей \n:pushpin:Зал "Бондюжский"'
#               '\n:minus::minus::minus::minus::minus::minus:'
#               '\nЭкскурсия\n:bust_in_silhouette:для тех, кто заехал 10 июля'
#               '\n\n:alarm_clock:<u><b>10:30 - 11:00</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>11:00 - 12:30</b></u>\nТренинг\n:bust_in_silhouette:для преподавателей \n:pushpin:Зал "Бондюжский"'
#               '\n:minus::minus::minus::minus::minus::minus:'
#               '\nЭкскурсия\n:bust_in_silhouette:для тех, кто заехал 10 июля'
#               '\n\n:alarm_clock:<u><b>12:30 - 13:30</b></u>\n:pot_of_food:Обед'
#               '\n\n:alarm_clock:<u><b>13:30 - 14:00</b></u>\nУстановочная встреча с участниками Форума\n📌 Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>14:00 - 16:00</b></u>\n:bust_in_silhouette:Группа А\nТренинг «Командообразование»\n📌 территория ДОЛ "Юность"'
#               '\n:minus::minus::minus::minus::minus::minus:'
#               '\n👤 Группа Б\nИнтенсив с элементами тренинга "Дизайн-мышление"\n📌 Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>16:00 - 16:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>16:30 - 18:30</b></u>'
#               '\n👤 Группа А\nИнтенсив с элементами тренинга "Дизайн-мышление"\n📌 Большой зал "Ромашкино"'
#               '\n:minus::minus::minus::minus::minus::minus:'
#               '\n:bust_in_silhouette:Группа Б\nТренинг «Командообразование»\n📌 территория ДОЛ "Юность"'
#               '\n\n:alarm_clock:<u><b>18:30 - 19:30</b></u>\n:pot_of_food:Ужин'
#               '\n\n:alarm_clock:<u><b>19:30 - 20:00</b></u>\n:FREE_button:Свободное время'
#               '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nТОРЖЕСТВЕННОЕ ОТКРЫТИЕ  4-го Международного нефтегазового '
#               'молодежного форума \n:pushpin:Футбольное поле')
#
# t12 = emojize('<u><b>Программа 12 июля</b> (Среда)</u>'
#               '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка "Силовая  Zymba"'
#               '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
#               '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nТренинг "Бизнес-моделирование"\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nТРЕНИНГ «ТрендЛаб»\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
#               '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nОТКРЫТЫЙ ЛЕКТОРИЙ\n:pushpin:Большой зал "Ромашкино"\nЭкспертная гостинная'
#               '\n:minus::minus::minus::minus::minus::minus:'
#               '\nУСТАНОВОЧНЫЙ семинар\n:bust_in_silhouette:с экспертами хакатона\n:pushpin:Зал Ново-Елховский'
#               '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nФорсайт сессия\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин'
#               '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nУстановочный тренинг на работу с кейсом\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nКультурно-развлекательная программа\nИнтеллектуальная игра'
#               '\n:pushpin:Большой зал "Ромашкино"')
#
# t13 = emojize('<u><b>Программа 13 июля</b> (Четверг)</u>'
#               '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка "Ритмы латина, бачата😍"'
#               '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
#               '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nТренинг "Креативная уверенность"\n:pushpin:Футбольное поле'
#               '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nЖеребьевка Хакатона. Представление экспертов. '
#               'Представление заданий и проведение жеребьевки среди команд.\n:pushpin:Футбольное поле'
#               '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
#               '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nХакатон Развития ТЭК 2050: Начало работы команд в малых группах'
#               '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nХакатон Развития ТЭК 2050: Продолжение работы команд'
#               '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин'
#               '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nЭкспертная гостинная:\n:pushpin: зал "Архангельский"'
#               '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nКультурно-развлекательная программа\n:pushpin:Футбольное поле')
#
# t14 = emojize('<u><b>Программа 14 июля</b> (Пятница)</u>'
#               '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка "Zymba+ силовая+ бачата"'
#               '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
#               '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nНЕФТЯНОЙ САММИТ Республики Татарстан\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nНЕФТЯНОЙ САММИТ Республики Татарстан\nДиалог на равных\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
#               '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nХакатон Развития ТЭК 2050: Продолжение работы команд\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nХакатон Развития ТЭК 2050: Продолжение работы команд\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин'
#               '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nТренинг "Успешная презентация перед инвестором"\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nЭкспертная гостиная\n:pushpin:Большой зал "Ромашкино"')
#
# t15 = emojize('<u><b>Программа 15 июля</b> (Суббота)</u>'
#               '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка "Zymba"'
#               '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
#               '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nХакатон Развития ТЭК 2050: Продолжение работы команд\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение со старожилом форума Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nХакатон Развития ТЭК 2050: Продолжение работы команд\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
#               '\n\n:alarm_clock:<u><b>14:00 - 14:30</b></u>\nПроведение жеребьёвки выступлений команд на предзащите\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>14:30 - 15:30</b></u>\nПРЕДЗАЩИТА ПРОЕКТНЫХ РЕШЕНИЙ (по 4-м направлениям)\n'
#               ':pushpin:4 зала (Ромашкино, Ново-Елховский, Бондюжский, Архангельский)'
#               '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение со старожилом форума Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nПРЕДЗАЩИТА ПРОЕКТНЫХ РЕШЕНИЙ (по 4-м направлениям)\n'
#               ':pushpin:4 зала (Ромашкино, Ново-Елховский, Бондюжский, Архангельский)'
#               '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин'
#               '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\nОБЪЯВЛЕНИЕ ФИНАЛИСТОВ.\nПроведение жеребьёвки выступлений '
#               'на финальной защите\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nСвободное время.\nКоманды-финалисты готовятся к финальное защите проектов')
#
# t16 = emojize('<u><b>Программа 16 июля</b> (Воскресенье)</u>'
#               '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка "Аэробика+ритмы "Тик-ток"'
#               '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
#               '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nФИНАЛ: ЗАЩИТА ПРОЕКТОВ\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение со старожилом форума Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nФИНАЛ: ЗАЩИТА ПРОЕКТОВ\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
#               '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nПОДВЕДЕНИЕ ИТОГОВ\nСовещание соревновательного жюри.'
#               '\nОбработка результатов голосования.\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение со старожилом форума Мистером Эчпочмаком'
#               '\n\n:alarm_clock:<u><b>16:00 - 17:00</b></u>\n:FREE_button:Свободное время'
#               '\n\n:alarm_clock:<u><b>17:00 - 18:00</b></u>\nОФИЦИАЛЬНОЕ ЗАКРЫТИЕ ФОРУМА.\nОБЪЯВЛЕНИЕ ПОБЕДИТЕЛЕЙ\n:pushpin:Большой зал "Ромашкино"'
#               '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин'
#               '\n\n:alarm_clock:<u><b>19:00 - 22:00</b></u>\nКультурная программа')
# t17 = emojize('<u><b>Программа 17 июля</b> (Понедельник)</u>'
#               '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак'
#               '\n\n:alarm_clock:<u><b>9:00 - 22:00</b></u>\n:airplane_departure:Отъезд участников'
#               '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед')

t10 = emojize('<u><b>Программа 10 июля</b> (Среда)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nТренинг\n:bust_in_silhouette:для преподавателей \n:pushpin:Универсальный зал 2 этаж'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nЭкскурсия\n:bust_in_silhouette:для тех, кто заехал 9 июля'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком\n:pushpin:Зона кофе-брейка 2,4 этаж'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nТренинг\n:bust_in_silhouette:для преподавателей \n:pushpin:Универсальный зал 2 этаж'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nЭкскурсия\n:bust_in_silhouette:для тех, кто заехал 9 июля'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед'
              '\n\n:alarm_clock:<u><b>14:00 - 15:30</b></u>\nЭкскурсия\n:bust_in_silhouette:для тех, кто заехал 10 июля'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком\n:pushpin:Зона кофе-брейка 2,4 этаж'
              '\n\n:alarm_clock:<u><b>16:00 - 18:00</b></u>\nЭкскурсия\n:bust_in_silhouette:для тех, кто заехал 10 июля'
              '\n\n:alarm_clock:<u><b>18:00 - 19:00</b></u>\n:pot_of_food:Ужин\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>19:00 - 20:00</b></u>\n:FREE_button:Свободное время'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nТОРЖЕСТВЕННОЕ ОТКРЫТИЕ 5-го Международного нефтегазового '
              'молодежного форума \n:pushpin:Амфитеатр')

t11 = emojize('<u><b>Программа 11 июля</b> (Четверг)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>9:00 - 9:30</b></u>\nУстановочная встреча с участниками Форума\n:pushpin:Атриум 1 этаж'
              '\n\n:alarm_clock:<u><b>9:30 - 13:00</b></u>\nТренинг "Командообразование"\n:pushpin:Территория кампуса АГТУ "ВШН"'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>14:00 - 16:00</b></u>\nМастер-класс группа "А" "Креативное мышление"\n:pushpin:Универсальный зал 2 этаж'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nМастер-класс группа "Б" "Публичные выступления и презентации"\n:pushpin:Помещение самостоятельной подготовки 4 этаж'
              '\n\n:alarm_clock:<u><b>16:00 - 16:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком\n:pushpin:Зона кофе-брейка 2,4 этаж'
              '\n\n:alarm_clock:<u><b>16:30 - 18:30</b></u>\nМастер-класс группа "Б" "Креативное мышление"\n:pushpin:Универсальный зал 2 этаж'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nМастер-класс группа "А" "Публичные выступления и презентации"\n:pushpin:Помещение самостоятельной подготовки 4 этаж'
              '\n\n:alarm_clock:<u><b>18:30 - 19:30</b></u>\n:pot_of_food:Ужин\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>19:30 - 20:00</b></u>\n:FREE_button:Свободное время'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nГруппа "А" Бизнес-симуляция "Битва корпораций"\n:pushpin:Помещение самостоятельной подготовки 4 этаж'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nГруппа "Б" Турнир "Время первых"\n:pushpin:Универсальный зал 2 этаж')

t12 = emojize('<u><b>Программа 12 июля</b> (Пятница)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>7:30 - 8:30</b></u>\n:pot_of_food:Завтрак\n:pushpin:Общежитие АГТУ ВШН (раздача ланч-боксов)'
              '\n\n:alarm_clock:<u><b>8:30 - 11:00</b></u>\nНЕФТЯНОЙ САММИТ Республики Татарстан\n:pushpin:Амфитеатр'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком\n:pushpin:Зона кофе-брейка 2,4 этаж'
              '\n\n:alarm_clock:<u><b>11:30 - 14:00</b></u>\nНЕФТЯНОЙ САММИТ Республики Татарстан диалог на равных с представителями бизнеса и власти\n:pushpin:Амфитеатр'
              '\n\n:alarm_clock:<u><b>14:00 - 15:00</b></u>\n:pot_of_food:Обед\n:pushpin:Общежитие АГТУ ВШН (раздача ланч-боксов)'
              '\n\n:alarm_clock:<u><b>15:00 - 16:00</b></u>\nХакатон Развития ТЭК 2050: Выдача кейсов. Проведение жеребьевки среди команд.\n:pushpin:Амфитеатр'
              '\n\n:alarm_clock:<u><b>16:00 - 18:30</b></u>\nФорсайт-сессия "Взгляд из будущего"\n:pushpin:Амфитеатр'
              '\n\n:alarm_clock:<u><b>18:30 - 19:30</b></u>\n:pot_of_food:Ужин\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>19:30 - 20:00</b></u>\n:FREE_button:Свободное время'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nГруппа "Б" Бизнес-симуляция "Битва корпораций"\n:pushpin:Помещение самостоятельной подготовки 4 этаж'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nГруппа "А" Турнир "Время первых"\n:pushpin:Универсальный зал 2 этаж')

t13 = emojize('<u><b>Программа 13 июля</b> (Суббота)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nМастер-класс "Как продать свою идею"\n:bust_in_silhouette:для участников Форума\n:pushpin:Амфитеатр'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nБрифинг\n:bust_in_silhouette:для менторов команд\n:pushpin:Универсальный зал 2 этаж'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком\n:pushpin:Зона кофе-брейка 2,4 этаж'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nХакатон Развития ТЭК 2050: Представление менторов команд, представление заданий и начало работы команд'
              '\n:pushpin:Трек №1 "Мировое технологическое лидерство в нефтегазодобыче" аудитория 4А38 - 4 этаж'
              '\n:pushpin:Трек №2 "Мировое технологическое лидерство в нефтегазопереработке и нефтегазохимии." аудитория 4А37 - 4 этаж'
              '\n:pushpin:Трек №3 "Индустриальные биотехнологии, композитные и биоразлагаемые материалы" аудитория 5А41 - 5 этаж'
              '\n:pushpin:Трек №4 "Цифровые технологии в нефтегазовом секторе." аудитория 5А40 - 5 этаж'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>14:00 - 16:00</b></u>\nХакатон Развития ТЭК 2050: продолжение работы команд\n:pushpin:Аудитории согласно треков'
              '\n\n:alarm_clock:<u><b>16:00 - 16:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком\n:pushpin:Зона кофе-брейка 2,4 этаж'
              '\n\n:alarm_clock:<u><b>16:30 - 18:30</b></u>\nХакатон Развития ТЭК 2050: продолжение работы команд\n:pushpin:Аудитории согласно треков'
              '\n\n:alarm_clock:<u><b>18:30 - 19:30</b></u>\n:pot_of_food:Ужин\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>19:30 - 20:00</b></u>\n:FREE_button:Свободное время'
              '\n\n:alarm_clock:<u><b>20:00 - 22:00</b></u>\nИнтеллектуальная игра "Requizit"\n:pushpin:Амфитеатр')

t14 = emojize('<u><b>Программа 14 июля</b> (Воскресенье)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>9:00 - 11:00</b></u>\nХакатон Развития ТЭК 2050: продолжение работы команд\n:pushpin:Аудитории согласно треков'
              '\n\n:alarm_clock:<u><b>11:00 - 11:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком\n:pushpin:Зона кофе-брейка 2,4 этаж'
              '\n\n:alarm_clock:<u><b>11:30 - 13:00</b></u>\nХакатон Развития ТЭК 2050: продолжение работы команд\n:pushpin:Аудитории согласно треков'
              '\n\n:alarm_clock:<u><b>13:00 - 14:00</b></u>\n:pot_of_food:Обед\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>14:00 - 16:00</b></u>\nХакатон Развития ТЭК 2050: продолжение работы команд\n:pushpin:Аудитории согласно треков'
              '\n:bust_in_silhouette:для участников'
              '\n:minus::minus::minus::minus::minus::minus:'
              '\nБрифинг\n:bust_in_silhouette:для экспертной комиссии по оценке кейсов\n:pushpin:Универсальный зал 2 этаж'
              '\n\n:alarm_clock:<u><b>16:00 - 16:30</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком\n:pushpin:Зона кофе-брейка 2,4 этаж'
              '\n\n:alarm_clock:<u><b>16:30 - 18:30</b></u>\nПОЛУФИНАЛ: ЗАЩИТА ПРОЕКТОВ\n:pushpin:Аудитории согласно треков'
              '\n\n:alarm_clock:<u><b>18:30 - 19:30</b></u>\n:pot_of_food:Ужин\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>19:30 - 20:00</b></u>\n:FREE_button:Свободное время'
              '\n\n:alarm_clock:<u><b>20:00 - 21:00</b></u>\nОБЪЯВЛЕНИЕ ФИНАЛИСТОВ. Проведение жеребьевки выступлений на финальной защите\n:pushpin:Амфитеатр'
              '\n\n:alarm_clock:<u><b>21:00 - 22:00</b></u>\nКоманды-финалисты готовятся к финальной защите проектов')

t15 = emojize('<u><b>Программа 15 июля</b> (Понедельник)</u>'
              '\n\n:alarm_clock:<u><b>7:15 - 7:45</b></u>\n:person_cartwheeling:Зарядка'
              '\n\n:alarm_clock:<u><b>8:00 - 9:00</b></u>\n:pot_of_food:Завтрак\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>9:00 - 10:30</b></u>\nХакатон Развития ТЭК 2050: подготовка к финальной защите проектов\n:pushpin:Аудитории согласно треков'
              '\n\n:alarm_clock:<u><b>10:30 - 11:00</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком\n:pushpin:Зона кофе-брейка 2,4 этаж'
              '\n\n:alarm_clock:<u><b>11:00 - 12:30</b></u>\nФИНАЛ: ЗАЩИТА ПРОЕКТОВ\n:pushpin:Атриум аудитория 6А.51 - 6 этаж'
              '\n\n:alarm_clock:<u><b>12:30 - 13:30</b></u>\n:pot_of_food:Обед\n:pushpin:Столовая'
              '\n\n:alarm_clock:<u><b>13:30 - 15:00</b></u>\nФИНАЛ: ЗАЩИТА ПРОЕКТОВ\n:pushpin:Атриум аудитория 6А.51 - 6 этаж'
              '\n\n:alarm_clock:<u><b>15:00 - 15:30</b></u>\nПОДВЕДЕНИЕ ИТОГОВ\nСовещание соревновательного жюри.\nОбработка результатов голосования.'
              '\n\n:alarm_clock:<u><b>15:30 - 16:00</b></u>\n:pie:Вкусное общение с Мистером Эчпочмаком\n:pushpin:Зона кофе-брейка 2,4 этаж'
              '\n\n:alarm_clock:<u><b>16:00 - 17:30</b></u>\nОткрытый диалог с участниками форума\n:pushpin:Амфитеатр'
              '\n\n:alarm_clock:<u><b>17:30 - 19:00</b></u>\nОФИЦИАЛЬНОЕ ЗАКРЫТИЕ ФОРУМА.\nОБЪЯВЛЕНИЕ ПОБЕДИТЕЛЕЙ\n:pushpin:Амфитеатр'
              '\n\n:alarm_clock:<u><b>19:00 - 22:00</b></u>\nКультурная программа\n:pushpin:Амфитеатр')

list_calendar = [t10, t11, t12, t13, t14, t15]
list_button = ['10.07/Ср', '11.07/Чт', '12.07/Пт', '13.07/Сб', '14.07/Вс', '15.07/Пн']


@dp.message_handler(text=emojize('Программа :tear-off_calendar:'))
async def calendar(msg: types.Message):
    day = datetime.datetime.now().strftime('%d')
    if 0 <= int(day) - 10 <= 6:
        mes = list_calendar[int(day) - 10]
    else:
        mes = list_calendar[0]
    kb_calendar = InlineKeyboardMarkup(row_width=3)
    for i in range(6):
        if i == int(day) - 10:
            kb_calendar.insert(InlineKeyboardButton(f'- {list_button[i]} -', callback_data='no'))
        else:
            kb_calendar.insert(InlineKeyboardButton(list_button[i], callback_data=cb_calendar.new(day=i)))
    await send_message_try(msg.from_user.id, mes, kb_calendar)


@dp.callback_query_handler(cb_calendar.filter())
async def calendar_day(call: types.CallbackQuery, callback_data: dict):
    mes = list_calendar[int(callback_data['day'])]
    kb_calendar = InlineKeyboardMarkup(row_width=3)
    for i in range(6):
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