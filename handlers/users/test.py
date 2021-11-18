from keyboards.inline.btn_menu import main_menu
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from states.cdzstate import Test
from aiogram import types
from mash import mesh
from loader import dp
import asyncio


@dp.callback_query_handler(text="pass_test", state=None)
async def bot_start(call: CallbackQuery):
    await call.message.edit_text("Отправьте ссылку на тест")
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    answers = mesh.get_answers(f"{answer}")
    await asyncio.sleep(1)
    for i in answers:
        await asyncio.sleep(1)
        await message.answer(f"***✏️ Задание***\n`└{i[0]}`\n\n 👑 Ответ:\n`└{i[1]}`")
    await message.answer("***Выдача ответов завершена!***\n"
                         "Вы автоматически вернулись в меню", reply_markup=main_menu)
    await state.finish()
