from config import *
from button import *
from func import *


def get_gallery_kb(page, photos) -> InlineKeyboardMarkup:
    kb_gallery = InlineKeyboardMarkup(row_width=3)
    has_next_page = len(photos) > page + 1
    if page != 0:
        kb_gallery.insert(InlineKeyboardButton(text="< Назад", callback_data=cb_photo.new(page=page - 1)))
    kb_gallery.insert(InlineKeyboardButton(text=f"{page + 1}/{len(photos)}", callback_data="dont_click_me"))
    if has_next_page:
        kb_gallery.insert(InlineKeyboardButton(text="Вперёд >", callback_data=cb_photo.new(page=page + 1)))
    kb_gallery.add(btn_send_photo)
    return kb_gallery


@dp.message_handler(text=emojize('Галерея :camera_with_flash:'))
async def gallery(msg: types.Message, page: int = 0):
    photos = session.query(Photo).all()
    if len(photos) > 0:
        kb_gallery = get_gallery_kb(page, photos)
        mes = emojize(f'Фото {page + 1}/{len(photos)}, автор: {photos[page].user.name}, {photos[page].date.strftime("%H:%M %d.%m.%Y г.")}')
        await bot.send_photo(msg.from_user.id, photos[page].file_id, mes, reply_markup=kb_gallery)
    else:
        mes = emojize('Пока тут нет ни одной фотографии. Загрузи первую.')
        kb_no_photo = InlineKeyboardMarkup()
        kb_no_photo.add(btn_send_photo)
        await bot.send_message(msg.from_user.id, mes, reply_markup=kb_no_photo)


@dp.callback_query_handler(cb_photo.filter())
async def photo_page_handler(call: types.CallbackQuery, callback_data: dict):
    page = int(callback_data['page'])
    photos = session.query(Photo).all()
    mes = emojize(f'Фото {str(page + 1)}/{len(photos)}, автор: {photos[page].user.name}, {photos[page].date.strftime("%H:%M %d.%m.%Y г.")}')
    kb_gallery = get_gallery_kb(page, photos)
    photo = InputMedia(type="photo", media=photos[page].file_id, caption=mes)
    await call.message.edit_media(photo, kb_gallery)
    await call.answer()


@dp.callback_query_handler(text='send_photo')
async def send_photo(call: types.CallbackQuery):
    await ipyforumStates.SEND_PHOTO.set()
    mes = emojize('Отправьте фото')
    await bot.send_message(call.from_user.id, mes)
    await call.answer()


@dp.message_handler(state=ipyforumStates.SEND_PHOTO, content_types=['photo'])
async def add_participant_db(msg: types.Message, state: FSMContext):
    await state.finish()
    file_id = msg.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    if not session.query(Photo).filter(Photo.file_path == file_path).first():
        new_photo = Photo(file_id=file_id, file_path=file_path, user_id=msg.from_user.id, date=datetime.datetime.now())
        session.add(new_photo)
        session.commit()
        mes = emojize('Ваше фото загружено. После подтверждения модератора фото будет добавлено в галерею.')
    else:
        mes = emojize('Такое фото уже есть в галерее')
    await bot.send_message(msg.from_user.id, mes)
    await gallery(msg=msg, page=len(session.query(Photo).all()) - 1)

