from aiogram.types import CallbackQuery

from keyboards.inline.back_btn import back_to_menu
from loader import dp


@dp.callback_query_handler(text="information")
async def get_security(call: CallbackQuery):
    await call.message.edit_text(
        f"***🗎 Лицензионное соглашение***\n"
        f"***1.0***\n"
        f"Пользуясь ботов, вы соглашаетесь с дейтвующими правила использования.\n"
        f"***1.1***\n"
        f"Аднинистрация не несёт ответсвтенность за любые денежные переводы и платежи "
        f"пользователй.\n"
        f"***1.2***\n"
        f"Аднинистрация имеет право отказать в предоставлении услуг пользоватлея без "
        f"указания причин.", reply_markup=back_to_menu)
