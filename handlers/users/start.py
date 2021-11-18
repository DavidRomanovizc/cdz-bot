from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from asyncpg import UniqueViolationError

from keyboards.inline.btn_menu import main_menu
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        await db.add_user_Users(full_name=message.from_user.full_name,
                                telegram_id=message.from_user.id,
                                username=message.from_user.username)
    except UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
        if user.get('is_banned') is not True:
            count_users = await db.count_users()
            await message.reply(text=(f"Приветствую вас, {message.from_user.full_name}!!\n"
                                      f"Это система для решения онлайн тестов на образовательных платформах РФ\n\n"),
                                reply_markup=main_menu)
        elif user.get('is_banned') is True:
            await message.answer(f'Вы заблокированы навсегда! За разблокировкой пишите админу')
