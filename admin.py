from config import *
from button import *
from func import *


async def is_admin(id):
    if session.query(User).filter(User.telegram_id == id).first().admin:
        return True
    else:
        return False


@dp.message_handler(commands=['listadmin'])
async def send_list_admin(msg: types.Message):
    if not await is_admin(msg.from_user.id):
        return
    await send_message_try(msg.from_user.id, 'Список администраторов:\n' + '\n'.join([i.name for i in get_admins()]))
