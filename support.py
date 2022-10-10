import bot
from config import *
from button import *
from func import *


@dp.message_handler(text=emojize('Помощь :red_question_mark:'))
async def support(msg: types.Message):
    mes = emojize('Здесь вы можете задать вопрос\n:nerd_face:<b>организаторам</b>')
    if get_user(msg.from_user.id).admin:
        count_no_answ = session.query(SupportQuestion).filter(SupportQuestion.answering == False).count()
        mes += emojize(f'\n\n<em>Неотвеченных вопросов - {str(count_no_answ)}</em>')
        await send_message_try(msg.from_user.id, mes, kb_no_answ)
    else:
        await send_message_try(msg.from_user.id, mes, kb_ask_quest)
    
    
@dp.callback_query_handler(text='send_question')
async def send_question(call: types.CallbackQuery):
    await ipyforumStates.SEND_QUEST.set()
    mes = emojize('Отправьте ваш вопрос или нажмите "Отмена" если передумали')
    kb_cancel = InlineKeyboardMarkup()
    kb_cancel.add(btn_cancel)
    await call.message.edit_text(mes, reply_markup=kb_cancel)
    
    
@dp.callback_query_handler(text='cancel', state=ipyforumStates.SEND_QUEST)
async def canceling(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()


@dp.message_handler(state=ipyforumStates.SEND_QUEST)
async def question_to_db(msg: types.Message, state: FSMContext):
    await state.finish()
    new_question = SupportQuestion(user_id=msg.from_user.id, text_question=msg.text)
    session.add(new_question)
    session.commit()
    mes = emojize('Спасибо! Ваш вопрос отправлен.\nВ ближайшее время \n:nerd_face:<b>организаторы</b> ответят на ваш вопрос.')
    await send_message_try(msg.from_user.id, mes)
    await support(msg=msg)
    user = get_user(msg.from_user.id)
    mes = emojize(f':police_car_light::police_car_light::police_car_light:\n<u>Пользователь :slightly_smiling_face:<b>{user.name}</b> спрашивает</u>:\n<em>{msg.text}</em>')
    kb_answ_quest = InlineKeyboardMarkup()
    kb_answ_quest.add(InlineKeyboardButton('Ответить', callback_data=cb_answ_quest.new(quest_id=new_question.id)))
    for i in get_admins():
        await send_message_try(i.telegram_id, mes, kb_answ_quest)


@dp.callback_query_handler(cb_answ_quest.filter())
async def support_answering(call: types.CallbackQuery, callback_data: dict):
    new_answer = SupportAnswer(admin_id=call.from_user.id, question_id=callback_data['quest_id'], date_anawer=datetime.datetime.now())
    session.add(new_answer)
    session.commit()
    admin = get_user(call.from_user.id)
    quest = session.query(SupportQuestion).filter(SupportQuestion.id == callback_data['quest_id']).first()
    mes = emojize(f':nerd_face:<b>{admin.name}</b>\nотвечает на вопрос пользователя\n:slightly_smiling_face:<b>{quest.user.name}</b>')
    for i in get_admins():
        await send_message_try(i.telegram_id, mes)
    await ipyforumStates.SEND_ANSWER.set()
    mes = emojize(f'Отправьте ответ на вопрос пользователя\n:slightly_smiling_face:<b>{quest.user.name}</b>:\n<em>{quest.text_question}</em>')
    await send_message_try(call.from_user.id, mes)
    await call.message.delete()


@dp.message_handler(state=ipyforumStates.SEND_ANSWER)
async def answer_to_db(msg: types.Message, state: FSMContext):
    await state.finish()
    answ = session.query(SupportAnswer).filter(SupportAnswer.admin_id == msg.from_user.id).order_by(desc(SupportAnswer.date_anawer)).first()
    session.query(SupportAnswer).filter(SupportAnswer.id == answ.id).update({'text_answer': msg.text}, synchronize_session='fetch')
    session.query(SupportQuestion).filter(SupportQuestion.id == answ.question.id).update({'answering':True}, synchronize_session='fetch')
    session.commit()
    mes = emojize(f':nerd_face:<b>{answ.admin.name}</b>\nответил(а) на ваш вопрос\n<em>"{answ.question.text_question}"</em>\n\n{msg.text}')
    await send_message_try(answ.question.user.telegram_id, mes)
    mes = emojize(f':nerd_face:<b>{answ.admin.name}</b>\nответил(а) на вопрос пользователя\n:slightly_smiling_face:<b>{answ.question.user.name}</b> \n<em>"{answ.question.text_question}"</em>\n\n{msg.text}')
    for i in get_admins():
        await send_message_try(i.telegram_id, mes)
    
    
@dp.callback_query_handler(text='no_answered')
async def no_answered(call: types.CallbackQuery):
    no_answ = session.query(SupportQuestion).filter(SupportQuestion.answering == False).all()
    if len(no_answ) > 0:
        for i in no_answ:
            mes = emojize(f':police_car_light::police_car_light::police_car_light:\n<u>Пользователь :slightly_smiling_face:<b>{i.user.name}</b> спрашивает</u>:\n<em>{i.text_question}</em>')
            kb_answ_quest = InlineKeyboardMarkup()
            kb_answ_quest.add(InlineKeyboardButton('Ответить', callback_data=cb_answ_quest.new(quest_id=i.id)))
            await send_message_try(call.from_user.id, mes, kb_answ_quest)
    else:
        await send_message_try(call.from_user.id, 'Нет неотвеченных вопросов')
    await call.answer()