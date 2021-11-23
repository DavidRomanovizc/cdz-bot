from keyboards.inline.btn_menu import main_menu
from asyncpg import UniqueViolationError
from aiogram.types import CallbackQuery
from loader import dp, db
import asyncio


@dp.callback_query_handler(text="stats")
async def get_stats(call: CallbackQuery):
    try:
        await db.add_user_Users(full_name=call.from_user.full_name,
                                telegram_id=call.from_user.id,
                                username=call.from_user.username)
    except UniqueViolationError:
        user = await db.select_user(telegram_id=call.from_user.id)
        if user.get('is_banned') is not True:
            count_users = await db.count_users()
            await call.message.delete()
            await call.message.answer_photo(
                photo=r"https://sun9-50.userapi.com/impg/qRmpnCNuxp2YwI3Yks8Bu5S-uOjqGQf8OTiaVg/4vU4GlZ6D_o.jpg?size=640x480&quality=96&sign=a31c6e1a0415112996db6c82f02c5fdb&type=album",
                caption=f"***📊 Статистика***\n"
                        f"- Количество пользователей: ***{count_users}***\n"
                        f"- Ваш Telegram ID: ***{call.from_user.id}***\n"
                        f"- Дата создания: ***14.11.2021***")
            await asyncio.sleep(1)
            await call.message.answer("Меню: ", reply_markup=main_menu)
