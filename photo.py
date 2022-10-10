from config import *
from button import *
from func import *


@dp.message_handler(text=emojize('Фото :camera_with_flash:'))
async def show_links_photo(msg: types.Message):
    links = session.query(LinkPhoto).order_by(LinkPhoto.date).all()
    if len(links) == 0:
        mes = emojize('Тут будут ссылки на альбомы с фотографиями. В скором времени они появятся.')
    else:
        mes = emojize('<b><u>Ссылки на альбомы с фотографиями:</u></b>')
        for i in links:
            mes += emojize(f'\n\n<b>{i.description}</b>\n<em>{i.link}</em>')
    if get_user(msg.from_user.id).admin:
        await send_message_try(msg.from_user.id, mes, kb_link_photo)
    else:
        await send_message_try(msg.from_user.id, mes)
    
    
@dp.callback_query_handler(text='add_link')
async def add_link(call: types.CallbackQuery):
    await ipyforumStates.ADD_LINK.set()
    mes = emojize('Отправьте ссылку')
    await send_message_try(call.from_user.id, mes)
    await call.answer()
    

@dp.message_handler(state=ipyforumStates.ADD_LINK)
async def add_link_db(msg: types.Message, state: FSMContext):
    if session.query(LinkPhoto).filter(LinkPhoto.link == msg.text).first():
        mes = emojize('Такая ссылка уже существует.')
        await msg.reply(mes)
        await state.finish()
        await show_links_photo(msg=msg)
    else:
        new_link = LinkPhoto(link=msg.text, admin_id=msg.from_user.id)
        session.add(new_link)
        session.commit()
        await ipyforumStates.DESC_LINK.set()
        mes = emojize('Отправьте опрсание к ссылке')
        await msg.reply(mes)


@dp.message_handler(state=ipyforumStates.DESC_LINK)
async def add_desc_to_link(msg: types.Message, state: FSMContext):
    await state.finish()
    link_id = session.query(LinkPhoto.id).filter(LinkPhoto.admin_id == msg.from_user.id).order_by(desc(LinkPhoto.date)).first()[0]
    session.query(LinkPhoto).filter(LinkPhoto.id == link_id).update({'description': msg.text}, synchronize_session='fetch')
    session.commit()
    mes = emojize('Ссылка добавлена.')
    await msg.reply(mes)
    await show_links_photo(msg=msg)
    

@dp.callback_query_handler(text='del_link')
async def choose_del_link(call: types.CallbackQuery):
    kb_del_link = InlineKeyboardMarkup(row_width=1)
    for i in session.query(LinkPhoto).all():
        kb_del_link.add(InlineKeyboardButton(f'{i.description}', callback_data=cb_link.new(link_id=i.id)))
    kb_del_link.add(btn_cancel)
    await call.message.edit_text('Выберите ссылку для удаления:', reply_markup=kb_del_link)
    await call.answer()
    
    
@dp.callback_query_handler(cb_link.filter())
async def del_link(call: types.CallbackQuery, callback_data: dict):
    session.query(LinkPhoto).filter(LinkPhoto.id == callback_data['link_id']).delete()
    session.commit()
    await call.message.edit_text('Ссылка удалена')
    await call.answer()
    
    
    
    