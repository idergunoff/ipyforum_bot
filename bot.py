from aiogram.utils import executor

from photo import *
from day_calendar import *
from support import *
from about import *
from map import *
from sammit import *
from admin import *


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    date_now = datetime.datetime.now()
    if not session.query(User).filter(User.telegram_id == msg.from_user.id).first():
        name_list = []
        if msg.from_user.first_name:
            name_list.append(msg.from_user.first_name)
        if msg.from_user.last_name:
            name_list.append(msg.from_user.last_name)
        user_name = ' '.join(name_list)
        new_user = User(telegram_id=msg.from_user.id, name=user_name, date_start=date_now, date_active=date_now)
        session.add(new_user)
    else:
        session.query(User).filter(User.telegram_id == msg.from_user.id).update({'date_active': date_now}, synchronize_session='fetch')
    session.commit()
    mes = emojize(msg.from_user.first_name + ", добро пожаловать в <b>ipyforum_bot</b>! :waving_hand:")
    await send_message_try(msg.from_user.id, mes, kb_start)
    
    
@dp.message_handler(commands=['be_admin'])
async def be_admin(msg: types.Message):
    kb_add_admin = InlineKeyboardMarkup(row_width=2)
    kb_add_admin.insert(InlineKeyboardButton('Да', callback_data=cb_add_admin.new(user_id=msg.from_user.id)))
    kb_add_admin.insert(InlineKeyboardButton('Нет', callback_data='no_admin'))
    user = session.query(User).filter(User.telegram_id == msg.from_user.id).first()
    mes = emojize(f'<b>{user.name}</b> запросил(а) права администратора. Предоставить?')
    for i in get_admins():
        await send_message_try(i.telegram_id, mes, kb_add_admin)
    mes = emojize('Вы запросили права администратора. Вы получите сообщение с результатом.')
    await send_message_try(msg.from_user.id, mes)
    
    
@dp.callback_query_handler(cb_add_admin.filter())
async def add_admin(call: types.CallbackQuery, callback_data: dict):
    admin = session.query(User).filter(User.telegram_id == call.from_user.id).first()
    user = session.query(User).filter(User.telegram_id == callback_data['user_id']).first()
    if get_user(callback_data['user_id']).admin:
        mes = 'Права уже предоставлены'
        await call.message.edit_text(mes)
    else:
        try:
            await call.message.delete()
        except:
            pass
        session.query(User).filter(User.telegram_id == callback_data['user_id']).update({'admin': True}, synchronize_session='fetch')
        session.commit()
        mes = emojize(f'<b>{admin.name}</b> предоставил(а) права администратора пользователю <b>{user.name}</b>')
        for i in get_admins():
            await send_message_try(i.telegram_id, mes)
            
    
@dp.callback_query_handler(text='no_admin')
async def no_admin(call: types.CallbackQuery):
    await call.message.delete()


@dp.message_handler(text=emojize('Чат :speech_balloon:'))
async def send_about(msg: types.Message):
    await send_message_try(msg.from_user.id, 'https://t.me/+bqE68NoGynI0MWIy\nПо этой ссылке-приглашению '
                                             'вы можете перейти в чат форума.', kb_start)


@dp.message_handler(text=emojize('Место 📍'))
async def send_location(message: types.Message):
    # Отправка геолокации с текстом
    latitude = 54.912790 # Широта
    longitude = 52.318390 # Долгота
    await bot.send_message(message.from_user.id, 'Площадка проведения форума - г. Альметьевск, кампус Альметьевского '
                                                 'государственного технологического университета «Высшая школа нефти»', reply_markup=kb_start)
    await bot.send_location(message.from_user.id, latitude, longitude)


@dp.message_handler(text=emojize('Заказать трансфер 🚌'))
async def get_transfer(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Для заказа трансфера заполните онлайн-форму: https://oprostn.ru/~ligHf', reply_markup=kb_start)

@dp.message_handler(text=emojize('Wi-Fi 📡'))
async def get_wifi(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Название сети:\nIPYForum-2024\n\nПароль:\nR4a-8Tdx', reply_markup=kb_start)


@dp.callback_query_handler(text='cancel')
async def canceling(call: types.CallbackQuery):
    await call.message.delete()


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)
