from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.back_btn import back_to_menu
from loader import dp, db


@dp.callback_query_handler(text="stats")
async def get_stats(call: CallbackQuery):
    id_ = call.from_user.id
    count_users = await db.count_users()
    await call.message.edit_text(f"***📊 Статистика***\n"
                                 f"- Количество пользователей: ***{count_users}***\n"
                                 f"- Ваш Telegram ID: ***{id_}***\n"
                                 f"- Дата создания: ***14.11.2021***", reply_markup=back_to_menu)