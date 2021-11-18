from aiogram.types import CallbackQuery

from keyboards.inline.btn_menu import main_menu
from loader import dp


@dp.callback_query_handler(text="back")
async def back_to_menu(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("Вы вернулись в меню: ", reply_markup=main_menu)