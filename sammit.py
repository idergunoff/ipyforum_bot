from config import *
from button import *
from func import *
import pandas as pd

#
# @dp.message_handler(text=emojize('Вопрос на Саммит :globe_with_meridians:'))
# async def summit(msg: types.Message):
#     await send_message_try(msg.from_user.id, '🛠 Программа Саммита на этапе разработки', kb_start)
#


@dp.message_handler(text=emojize('Вопрос на Саммит :globe_with_meridians:'))
async def summit(msg: types.Message):
    mes = emojize('В рамках Нефтяного Саммита Республики Татарстан 2024 состоится панельная дискуссия: '
        '<b>«Топливно-энергетический комплекс России 2050: Технологическое лидерство как ключевой драйвер устойчивого будущего»</b> '
        '\n\nКлючевые темы для обсуждения: '
        '\n<i>- Мировое технологическое лидерство в нефтегазодобыче, нефтепереработке и нефтегазохимии'
        '\n- Цифровые технологии в нефтегазовом секторе'
        '\n- Повышение устойчивости нефтегазовой отрасли и развитие новых бизнес-направлений: индустриальные биотехнологии, композитные материалы и др.</i>'
        '\n\nУчастники панельной дискуссии:'
        '\nМодератор: '
        '\n<b>КАШУРНИКОВА Александра Александровна</b>, Ведущая Российского общества Знание, продакшн Молодёжного направления Общероссийского Общественного движения «Народный фронт «За Россию»'
        '\n\nУчастники-спикеры: '
        '\n<b>ЦИВИЛЕВ Сергей Евгеньевич</b>, Министр энергетики Российской Федерации'
        '\n\n<b>МИННИХАНОВ Рустам Нургалиевич</b>, Раис Республики Татарстан'
        '\n\n<b>ЯНОВСКИЙ Анатолий Борисович</b>, Руководитель рабочей группы по вопросам экологической безопасности Комиссии при Президенте Российской Федерации по вопросам стратегии развития топливно-энергетического комплекса и экологической безопасности'
        '\n\n<b>ШАФРАНИК Юрий Константинович</b>, Председатель Совета Союза нефтегазопромышленников России'
        '\n\n<b>РЫБАКОВ Андрей Алексеевич</b>, Председатель Белорусского государственного концерна по нефти и химии «Белнефтехим»'
        '\n\n<b>МАГАНОВ Наиль Ульфатович</b>, Генеральный директор ПАО «Татнефть»'
        '\n\n<b>ОРИПОВА Азиза Алишеровна</b>, Заместитель директора ПИШ ИТМО, руководитель образовательной программы «Индустриальная биотехнология» Высшей школы нефти -ИТМО'
        '\n\nНиже вы можете задать вопрос одному из спикеров и он обязательно будет озвучен в рамках дискуссии')
    if get_user(msg.from_user.id).admin:
        count_quest = session.query(SummitQuestion).count()
        mes += emojize(f'\n\n<em><u>Количество вопросов в базе данных - {str(count_quest)}</u></em>')
        await send_message_try(msg.from_user.id, mes, kb_summit_admin)
    else:
        await send_message_try(msg.from_user.id, mes, kb_summit)


@dp.callback_query_handler(text='quest_summit')
async def choose_participant(call: types.CallbackQuery):
    mes = emojize('Выберите участника-спикера, которому вы задаете вопрос:')
    await send_message_try(call.from_user.id, mes, kb_part)
    await call.answer()


@dp.callback_query_handler(text='cancel')
async def canceling(call: types.CallbackQuery):
    await call.message.delete()


@dp.callback_query_handler(cb_part.filter())
async def send_question_to_summit(call: types.CallbackQuery, callback_data: dict):
    u_name = session.query(User.name).filter(User.telegram_id == call.from_user.id).first()[0]
    new_summit_quest = SummitQuestion(user_id=call.from_user.id, who_question=callback_data['name'],
                                      date_question=datetime.datetime.now(), user_name=u_name)
    session.add(new_summit_quest)
    session.commit()
    await ipyforumStates.SUMMIT.set()
    mes = emojize(f'Отправьте ваш вопрос для спикера <b>{callback_data["name"]}</b>')
    await call.message.edit_text(mes)


@dp.message_handler(state=ipyforumStates.SUMMIT)
async def question_to_db(msg: types.Message, state: FSMContext):
    await state.finish()
    summit_quest = session.query(SummitQuestion).filter(SummitQuestion.user_id == msg.from_user.id).order_by(desc(SummitQuestion.date_question)).first()
    session.query(SummitQuestion).filter(SummitQuestion.id == summit_quest.id).update({'text_question':msg.text}, synchronize_session='fetch')
    session.commit()
    mes = emojize(f'Поздравляем!\nВы отправили вопрос для участника саммита <b>{summit_quest.who_question}</b>:\n<em>{msg.text}</em>\n')
    await send_message_try(msg.from_user.id, mes)


@dp.callback_query_handler(text='get_quests')
async def get_quests(call: types.CallbackQuery):
    table = pd.read_sql(session.query(SummitQuestion).statement, session.bind)
    table.to_excel('Вопросы на саммит.xlsx')
    await bot.send_document(call.from_user.id, open('Вопросы на саммит.xlsx', 'rb'))
    await call.answer()