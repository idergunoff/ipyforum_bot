from aiogram.utils import exceptions

from config import *


def get_user(teleg_id):
    return session.query(User).filter(User.telegram_id == teleg_id).first()


def get_admins():
    return session.query(User).filter(User.admin == True).all()


async def send_message_try(id, mesage, kb=False):
    try:
        if kb:
            await bot.send_message(id, mesage, reply_markup=kb)
        else:
            await bot.send_message(id, mesage)
    except exceptions.BotBlocked:
        session.query(User).filter(User.telegram_id == id).delete()
        session.commit()



