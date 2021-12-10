from keyboards.inline.btn_menu import main_menu
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.payment_methods import buy_sub
from states.cdzstate import Test
from aiogram import types
from utils.mash import mesh
from loader import dp, db
import asyncio


@dp.callback_query_handler(text="pass_test", state=None)
async def bot_start(call: CallbackQuery):
    await call.answer(cache_time=60)
    user = await db.select_user(telegram_id=call.from_user.id)
    is_premium = user.get('is_premium')
    if is_premium is True:
        await call.message.edit_text("Отправьте ссылку на тест")
        await Test.Q1.set()
    else:
        await call.message.edit_text("Вам нужно приобрести подписку", reply_markup=buy_sub)


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    answers = mesh.get_answers(f"{answer}")
    user = await db.select_user(telegram_id=message.from_user.id)
    is_premium = user.get('is_premium')
    if is_premium is True:
        await asyncio.sleep(1)
        for i in answers:
            await asyncio.sleep(1)
            await message.answer(f"***✏️ Задание***\n`└{i[0]}`\n\n 👑 Ответ:\n`└{i[1]}`")
        await message.answer("***Выдача ответов завершена!***\n"
                             "Вы автоматически вернулись в меню", reply_markup=main_menu)
        await state.finish()

    else:
        await message.answer("Вам нужно приобрести подписку", reply_markup=buy_sub)
