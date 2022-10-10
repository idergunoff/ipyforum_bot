from config import *
from button import *
from func import *


text1 = emojize(':index_pointing_up::nerd_face: 3-й Международный нефтегазовый молодежный форум – уникальная образовательная площадка, целью которой '
                'является выявление и развитие прогрессивной команды талантливой молодежи для решения актуальных задач, '
                'стоящих перед топливно-энергетическим комплексом России и стран ближнего зарубежья.')
text2 = emojize(':index_pointing_up::nerd_face: Главным мероприятием данного Форума станет уникальная образовательная программа в формате хакатона '
                '«Хакатон-Развитие ТЭК 2022», которая состоит из шестидневного интенсива: самостоятельных треков, '
                'мастер-классов ведущих экспертов нефтегазовой сферы, блиц-хакатонов, деловых игр. Участников обучат '
                'принципам Agile, методике Scrum и Kanban,проектному управлению, основам гибкого мышления и ТРИЗ. '
                'Особое внимание при этом будет уделено развитию soft skills: лидерству, эффективной коммуникации, '
                'ориентации на результат.')
text3 = emojize(':index_pointing_up::nerd_face: На хакатоне участники будут объединены в международные команды для решения актуальных задач ТЭК '
                'России и бизнес-вызовов нефтегазовой отрасли. За каждой командой будет закреплен модератор из числа '
                'преподавателей.')
text4 = emojize(':index_pointing_up::nerd_face: В формате блиц-хакатонов 250 участников - молодых специалистов, ученых, преподавателей, аспирантов, '
                'магистров и студентов ведущих вузов (направлений «Химические технологии», «Нефтегазовое дело», '
                '«Промышленная экология и биотехнология», «Экология и природопользование», «Биоинженерия и '
                'биоинформатика», «Биотехнология», «Энерго- и ресурсосберегающие процессы химической технологии, '
                'нефтехимии и биотехнологии», «Информационные технологии» (работа с большими данными)» в возрасте от '
                '18 до 35 лет будут решать реальные бизнес-задачи, стоящие перед ведущими нефтегазовыми компаниями '
                'России и ближнего зарубежья.')
text5 = emojize(':index_pointing_up::nerd_face: Также в рамках Форума 12 июля пройдет Нефтяной саммит Республики Татарстан с участием Президента '
                'Республики Татарстан Рустама Минниханова. Темой Саммита в 2022 году станет устойчивое развитие '
                'нефтегазовой отрасли в контексте диверсификации и технологического лидерства, в рамках панельной '
                'дискуссии и других мероприятий будет обсуждаться поиск решений наиболее актуальных задач ТЭК-2022, '
                'вопросы ESG-трансформации, новые технологии энергоресурсосбережения, а также применение биотехнологий '
                'в нефтегазовой отрасли.')
text6 = emojize(':index_pointing_up::nerd_face: Организаторами форума являются Минэнерго России, ПАО «Татнефть», Молодежный совет нефтегазовой '
                'отрасли при Минэнерго России, оператором – Национальный фонд подготовки кадров.')


list_text = [text1, text2, text3, text4, text5, text6]
list_button = [emojize(':one:', language='alias'), emojize(':two:', language='alias'),
               emojize(':three:', language='alias'), emojize(':four:', language='alias'),
               emojize(':five:', language='alias'), emojize(':six:', language='alias')]


@dp.message_handler(text=emojize('О форуме :placard:'))
async def send_about(msg: types.Message, page=0):
    kb_about = InlineKeyboardMarkup(row_width=3)
    for i in range(6):
        if i == page:
            kb_about.insert(InlineKeyboardButton(f'- {list_button[i]} -', callback_data='no'))
        else:
            kb_about.insert(InlineKeyboardButton(list_button[i], callback_data=cb_about.new(page=i)))
    await send_message_try(msg.from_user.id, list_text[page], kb_about)


@dp.callback_query_handler(cb_about.filter())
async def page_about(call: types.CallbackQuery, callback_data: dict):
    page = int(callback_data['page'])
    kb_about = InlineKeyboardMarkup(row_width=3)
    for i in range(6):
        if i == page:
            kb_about.insert(InlineKeyboardButton(f'- {list_button[i]} -', callback_data='no'))
        else:
            kb_about.insert(InlineKeyboardButton(list_button[i], callback_data=cb_about.new(page=i)))
    await call.message.edit_text(list_text[page], reply_markup=kb_about)
    await call.answer()


@dp.callback_query_handler(text='no')
async def no(call: types.CallbackQuery):
    await call.answer()

