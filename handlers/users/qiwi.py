import asyncio
from typing import Union

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from glQiwiApi import types as qiwi_types

from keyboards.inline.btn_menu import main_menu
from keyboards.inline.payment_methods import pay_Qiwi
from loader import wallet, dp, db, bot


async def create_payment(amount: Union[float, int] = 1) -> qiwi_types.Bill:
    async with wallet:
        return await wallet.create_p2p_bill(amount=amount)


@dp.callback_query_handler(text="pay_balance")
async def get_payment(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text("***💳 Стоимость подписки:***\n"
                                 "├Навсегда [[59₽]]\n"
                                 "├Чтобы проверить актуальность цен, нажмите на кнопку \n***├🔄 Проверить цены***\n"
                                 "├Если у вас нет Qiwi или нет возможности оплатить с помощью ├киви, то нажмите"
                                 "на кнопку\n"
                                 "├🆘 Контакт поддержки",
                                 reply_markup=pay_Qiwi)


@dp.callback_query_handler(text="check_price")
async def check_price(call: CallbackQuery):
    await bot.answer_callback_query(call.id, text="✔️ Цена актуальна")


@dp.callback_query_handler(text='pay_qiwi')
async def payment(message: Union[CallbackQuery, types.Message], state: FSMContext):
    await message.answer(cache_time=60)
    user = await db.select_user(telegram_id=message.from_user.id)
    try:
        is_premium = user.get('is_premium')
        print(is_premium)
    except AttributeError:
        is_premium = False
    bill = await create_payment()
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Оплатить', url=bill.pay_url)
    keyboard.add(btn1)
    btn2 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='check_payment')
    keyboard.add(btn2)
    btn3 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel_payment')
    keyboard.add(btn3)
    if is_premium is True:
        await bot.send_message(message.from_user.id, text=f"Поздравляю! Доступ уже куплен :)")
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id, text=f"👑 Приветствуем вас, {message.from_user.full_name}!\n\n"
                                                          f"🖥️ Это система для решения ***онлайн тестов*** на "
                                                          f"образовательных платформах РФ\n\n "
                                                          f"Бот не может решать тесты, где есть ***задания открытого "
                                                          f"типа***\n",
                               reply_markup=main_menu)

    else:
        await bot.send_message(message.from_user.id, text=f"После оплаты нажми ***Проверить оплату***\n"
                                                          f"Если не получается оплатить по странице ниже, "
                                                          f"напиши сюда: @DRomanovizc",
                               reply_markup=keyboard)
        await state.set_state("payment")
        await state.update_data(bill=bill)


@dp.callback_query_handler(state="payment", text="check_payment")
async def successful_payment(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Проверить оплату', callback_data='check_payment')
    keyboard.add(btn1)
    keyboard1 = types.ReplyKeyboardMarkup()
    async with state.proxy() as data:
        bill: qiwi_types.Bill = data.get("bill")
    status = await bill.check()
    if status:
        await call.message.edit_text("Оплата прошла успешно!")
        await db.update_premiun(telegram_id=call.from_user.id, is_premium=True)
        await state.finish()

    else:
        await call.message.answer("Оплата не прошла! Подождите минут 10, а затем еще раз попробуйте нажать кнопку ниже",
                                  reply_markup=keyboard)


@dp.callback_query_handler(state='payment', text='cancel_payment')
async def cancel_payment(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.reply(f'Вы отменили покупку :(\n', reply_markup=main_menu)
    await state.reset_state()
