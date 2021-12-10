from keyboards.inline.guide_btn import first_str, second_str, third_str, fourth_str
from aiogram.types import CallbackQuery, InputMediaPhoto
from loader import dp, bot


@dp.callback_query_handler(text="guide_btn")
async def get_information(call: CallbackQuery):
    await call.answer(cache_time=60)
    photo = r"https://sun9-61.userapi.com/impg/eUV4dgTgCstwBeOMA01QhMdmeb_UWEzy9Q-VaQ/g9x97DW8iHE.jpg?size=1185x1278&quality=96&sign=ba60d485581c09089440d057aa74d7d8&type=album"
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.send_photo(chat_id=call.from_user.id,
                         photo=photo,
                         caption="Руководство по боту: \n***Страница №1***", reply_markup=first_str)


@dp.callback_query_handler(text="forward_f")
async def get_forward(call: CallbackQuery):
    await call.answer(cache_time=60)
    photo = InputMediaPhoto(
        "https://sun9-53.userapi.com/impg/SLGs9kpZmAExRpmEJ8RCCQtBc7Ckoc6sG7QWgA/73HolD9HQo4.jpg?size=1185x1278&quality=96&sign=969985c265d7a6d1215cbaa334f1fa33&type=album",
        caption="Руководство по боту: \n***Страница №2***")
    await call.message.edit_media(photo, reply_markup=second_str)


@dp.callback_query_handler(text="backward_s")
async def get_backward_f(call: CallbackQuery):
    await call.answer(cache_time=60)
    photo = InputMediaPhoto(
        "https://sun9-61.userapi.com/impg/eUV4dgTgCstwBeOMA01QhMdmeb_UWEzy9Q-VaQ/g9x97DW8iHE.jpg?size=1185x1278&quality=96&sign=ba60d485581c09089440d057aa74d7d8&type=album",
        caption="Руководство по боту: \n***Страница №1***"
    )
    await call.message.edit_media(photo, reply_markup=first_str)


@dp.callback_query_handler(text="forward_s")
async def get_forward_s(call: CallbackQuery):
    await call.answer(cache_time=60)
    photo = InputMediaPhoto(
        "https://sun9-1.userapi.com/impg/3d_HLxu7T6_AKdZPPp0PaCBzK8b568RcouVH-g/GWMBuVx4k9E.jpg?size=1185x1278&quality=96&sign=a02574db5949e1b5d96721ff4c4f25fd&type=album",
        caption="Руководство по боту: \n***Страница №3***")
    await call.message.edit_media(photo, reply_markup=third_str)


@dp.callback_query_handler(text="backward_th")
async def get_backward_f(call: CallbackQuery):
    await call.answer(cache_time=60)
    photo = InputMediaPhoto(
        "https://sun9-53.userapi.com/impg/SLGs9kpZmAExRpmEJ8RCCQtBc7Ckoc6sG7QWgA/73HolD9HQo4.jpg?size=1185x1278&quality=96&sign=969985c265d7a6d1215cbaa334f1fa33&type=album",
        caption="Руководство по боту: \n***Страница №2***"
    )
    await call.message.edit_media(photo, reply_markup=second_str)


@dp.callback_query_handler(text="forward_th")
async def get_backward_f(call: CallbackQuery):
    await call.answer(cache_time=60)
    photo = InputMediaPhoto(
        "https://sun9-81.userapi.com/impg/zBNvtkT57P-vwWImwfPSsRohU1CPc7lCJI9AYw/Jpk5NceOvPA.jpg?size=1185x1278&quality=96&sign=d35f35011dae6b0d3e8e9d7fd37534e2&type=album",
        caption="Руководство по боту: \n***Страница №4***"
    )
    await call.message.edit_media(photo, reply_markup=fourth_str)


@dp.callback_query_handler(text="backward_four")
async def get_backward_f(call: CallbackQuery):
    await call.answer(cache_time=60)
    photo = InputMediaPhoto(
        "https://sun9-1.userapi.com/impg/3d_HLxu7T6_AKdZPPp0PaCBzK8b568RcouVH-g/GWMBuVx4k9E.jpg?size=1185x1278&quality=96&sign=a02574db5949e1b5d96721ff4c4f25fd&type=album",
        caption="Руководство по боту: \n***Страница №3***"
    )
    await call.message.edit_media(photo, reply_markup=third_str)
