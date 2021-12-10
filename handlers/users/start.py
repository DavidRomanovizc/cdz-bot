from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.btn_menu import main_menu
from asyncpg import UniqueViolationError
from aiogram import types
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        await db.add_user_Users(full_name=message.from_user.full_name,
                                telegram_id=message.from_user.id,
                                username=message.from_user.username)
        user = await db.select_user(telegram_id=message.from_user.id)
        is_premium = user.get('is_premium')
        if is_premium:
            prime_status = "Куплена"
        else:
            prime_status = "Не куплена"

        await message.reply(text=(f"Приветствуем вас, {message.from_user.full_name}!\n\n"
                                  f"💸Подписка: ***{prime_status}***\n\n"
                                  f"Это система для решения онлайн тестов на образовательных платформах РФ\n\n"
                                  f"Бот не может решать тесты, где есть задания ***открытого типа***\n"),
                            reply_markup=main_menu)

    except UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
        is_premium = user.get('is_premium')
        if is_premium:
            prime_status = "Куплена"
        else:
            prime_status = "Не куплена"
        await message.reply(text=(f"Приветствуем вас, {message.from_user.full_name}!\n\n"
                                  f"💸 Подписка: ***{prime_status}***\n\n"
                                  f"Это система для решения онлайн тестов на образовательных платформах РФ\n\n"
                                  f"Бот не может решать тесты, где есть задания ***открытого типа***\n"),
                            reply_markup=main_menu)
