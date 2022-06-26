from aiogram.utils import executor

from gallery import *
from day_calendar import *


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
    await bot.send_message(msg.from_user.id, mes, reply_markup=kb_start)


@dp.message_handler(text=emojize('О форуме :placard:'))
async def send_about(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Здесь будет тескт о форуме.')


@dp.message_handler(text=emojize('Карта :world_map:'))
async def send_map(msg: types.Message):
    await bot.send_document(msg.from_user.id, open('map.jpg', 'rb'))


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)
