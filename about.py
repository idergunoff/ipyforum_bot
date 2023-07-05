from config import *
from button import *
from func import *


text1 = emojize(':index_pointing_up::nerd_face: 4-й Международный нефтегазовый молодежный форум – это уникальная '
                'образовательная площадка, целью которой является выявление и развитие прогрессивной команды талантливой '
                'молодежи для решения актуальных задач, стоящих перед топливно-энергетическим комплексом России и стран ближнего зарубежья.')
text2 = emojize(':index_pointing_up::nerd_face: Традиционно организаторами Форума выступают Министерство энергетики '
                'Российской Федерации, ПАО «Татнефть», Молодежный совет нефтегазовой отрасли при Минэнерго России. '
                'Оператор образовательной программы – Национальный фонд подготовки кадров (НФПК).')
text3 = emojize(':index_pointing_up::nerd_face: Четвертый Международный нефтегазовый молодежный форум '
                '«4th INTERNATIONAL PETROLEUM YOUTH FORUM» – Хакатон Развития ТЭК 2050 пройдет в г. Альметьевск '
                'Республики Татарстан с 11 по 17 июля 2023 года.')
text4 = emojize(':index_pointing_up::nerd_face: Целевая аудитория Форума – молодые специалисты компаний ТЭК России и '
                'стран ближнего и дальнего зарубежья, молодые ученые и преподаватели, аспиранты и студенты ведущих '
                'нефтегазовых образовательных учреждений высшего профессионального образования. Участники Форума '
                'в течение шести дней пройдут интенсивное обучение, предусматривающее сессии, мастер-классы ведущих '
                'экспертов нефтегазовой сферы, тренинги, позволяющие принять активное участие в рассмотрении '
                'бизнес-вызовов и кейсов по поиску решений и выявлению наиболее актуальных проблем, связанных с '
                'технологическим лидерством в нефтегазодобыче, нефтепереработке и нефтегазохимии, в том числе '
                'в вопросах, связанных с декарбонизацией цепочек создания стоимости и ESG повестки, повышения '
                'устойчивости нефтегазовой отрасли за счет развития сферы индустриальных биотехнологий и композитных материалов.  ')
text5 = emojize(':index_pointing_up::nerd_face: Форум будет проходить в формате хакатона и станет не только '
                'дискуссионной площадкой для молодых профессионалов, но и «точкой сбора» инициатив молодых специалистов '
                'из разных отраслей и регионов по формированию и продвижению мировоззрения технологического лидерства '
                'ТЭК России вплоть до 2050 года. Лучшие предложения и проектные идеи международных команд получат '
                'финансовую и менторскую поддержку.')
text6 = emojize(':index_pointing_up::nerd_face: Также в рамках Форума, 14 июля 2023 года состоится традиционный '
                'Нефтяной саммит Республики Татарстан (далее – Саммит). За свою двадцатилетнюю историю Саммит стал '
                'одной из наиболее авторитетных российских дискуссионных площадок, на которой обсуждаются актуальные '
                'вопросы развития нефтяной отрасли, находятся новые точки роста экономики, формулируется '
                'консолидированная позиция власти и бизнеса по ключевым вопросам.')


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

