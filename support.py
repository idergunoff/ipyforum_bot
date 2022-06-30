import bot
from config import *
from button import *
from func import *


@dp.message_handler(text=emojize('Помощь :red_question_mark:'))
async def support(msg: types.Message):
    mes = emojize('Здесь вы можете задать вопрос организаторам')
    await bot.send_message(msg.from_user.id, mes, reply_markup=kb_ask_quest)
    
    
@dp.callback_query_handler(text='send_question')
async def send_question(call: types.CallbackQuery):
    await ipyforumStates.SEND_QUEST.set()
    mes = emojize('Отправьте ваш вопрос или нажмите "Отмена" если передумали')
    await call.message.edit_text(mes)


@dp.message_handler(state=ipyforumStates.SEND_QUEST)
async def question_to_db(msg: types.Message, state: FSMContext):
    await state.finish()
    new_question = SupportQuestion(user_id=msg.from_user.id, text_question=msg.text)
    session.add(new_question)
    session.commit()
    mes = emojize('Спасибо! Ваш вопрос отправлен. В ближайшее время организаторы ответят на ваш вопрос.')
    await bot.send_message(msg.from_user.id, mes)
    await support(msg=msg)
    user = get_user(msg.from_user.id)
    mes = emojize(f':police_car_light::police_car_light::police_car_light:\n<u>Пользователь <b>{user.name}</b> спрашивает</u>:\n<em>{msg.text}</em>')
    kb_answ_quest = InlineKeyboardMarkup()
    kb_answ_quest.add(InlineKeyboardButton('Ответить', callback_data=cb_answ_quest.new(quest_id=new_question.id)))
    for i in get_admins():
        await bot.send_message(i.telegram_id, mes, reply_markup=kb_answ_quest)


@dp.callback_query_handler(cb_answ_quest.filter())
async def support_answering(call: types.CallbackQuery, callback_data: dict):
    new_answer = SupportAnswer(admin_id=call.from_user.id, question_id=callback_data['quest_id'])
    session.add(new_answer)
    session.commit()
    admin = get_user(call.from_user.id)
    quest = session.query(SupportQuestion).filter(SupportQuestion.id == callback_data['quest_id']).first()
    mes = emojize(f'<b>{admin.name}</b> отвечает на вопрос пользователя <b>{quest.user.name}</b>')
    for i in get_admins():
        await bot.send_message(i.telegram_id, mes)
    await ipyforumStates.SEND_ANSWER.set()
    mes = emojize('Отправьте ответ')
    await bot.send_message(call.from_user.id, mes)
    await call.answer()

    