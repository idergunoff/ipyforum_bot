from config import *
from button import *
from func import *


text_map1 = emojize('1. Административный корпус\n2. Корпус №1\n3. Корпус №3\n4. Корпус №4\n5. Корпус №5\n6. Корпус №6'
                   '\n7. Большой зал "Архангельский"\n8. Столовая\n9. Саммит-холл\n10. Площадка для отдыха'
                   '\n11. Зона выставки\n12. Теннисный корт\n13. Футбольное поле\n14. Беседка\n15. Конюшня\n16. КПП')
text_map2 = emojize('1 этаж')
text_map3 = emojize('2 этаж')
text_map4 = emojize('3 этаж')

list_map = [['AgACAgIAAxkBAAIEl2LIrOwKdM6n8a0KCuL93a7VJhSbAAL7vzEbqUlISlQ9aFWGdtwlAQADAgADeQADKQQ', text_map1],
            ['AgACAgIAAxkBAAIEmGLIrSgpBe_sj97TftabGMZZNDVCAAL9vzEbqUlIShtTJEvnGznNAQADAgADeQADKQQ', text_map2],
            ['AgACAgIAAxkBAAIEmWLIrXLCzSjXClbM_74su2NKx3yaAAL-vzEbqUlISk3F8jmIv11CAQADAgADeQADKQQ', text_map3],
            ['AgACAgIAAxkBAAIEmmLIrZvwKsbAS714gK4lntj6U6TkAAL_vzEbqUlISuJ_hFI4Je8IAQADAgADeQADKQQ', text_map4]]
list_button = ['Схема ДОЛ Юность', emojize('Саммит-холл :one:', language='alias'),
               emojize('Саммит-холл :two:', language='alias'),
               emojize('Саммит-холл :three:', language='alias')]


@dp.message_handler(text=emojize('Схема кампуса :world_map:'))
async def send_map(msg: types.Message):
    await send_message_try(msg.from_user.id, '🛠 На данный момент схема форума находится в разработке', kb_start)


# @dp.message_handler(text=emojize('Схема кампуса :world_map:'))
# async def send_map(msg: types.Message, page=0):
#     kb_map = InlineKeyboardMarkup(row_width=2)
#     for i in range(4):
#         if i == page:
#             kb_map.insert(InlineKeyboardButton(f'- {list_button[i]} -', callback_data='no'))
#         else:
#             kb_map.insert(InlineKeyboardButton(list_button[i], callback_data=cb_map.new(page=i)))
#     await bot.send_photo(msg.from_user.id, list_map[page][0], caption=list_map[page][1], reply_markup=kb_map)
#

@dp.callback_query_handler(cb_map.filter())
async def page_map(call: types.CallbackQuery, callback_data: dict):
    page = int(callback_data['page'])
    kb_map = InlineKeyboardMarkup(row_width=2)
    for i in range(4):
        if i == page:
            kb_map.insert(InlineKeyboardButton(f'- {list_button[i]} -', callback_data='no'))
        else:
            kb_map.insert(InlineKeyboardButton(list_button[i], callback_data=cb_map.new(page=i)))
    await call.message.edit_media(InputMedia(type="photo", media=list_map[page][0], caption=list_map[page][1]), reply_markup=kb_map)
    await call.answer()


@dp.callback_query_handler(text='no')
async def no(call: types.CallbackQuery):
    await call.answer()

