from keyboards.inline.btn_menu import main_menu
from aiogram.types import CallbackQuery
from loader import dp, bot


@dp.callback_query_handler(text="back")
async def back_to_menu(call: CallbackQuery):
    await call.message.edit_text("***👨‍💻 Cdz.Bot*** - телеграм бот, который может решать цдз тесты\n\n"
                                 "***🤝 Сотрудничество:***\n"
                                 "Если у вас есть предложение о сотрудничестве, пишите сюда - "
                                 "@DRomanovizc", reply_markup=main_menu)


@dp.callback_query_handler(text="close_everything")
async def get_close_everything(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("***👨‍💻 Cdz.Bot*** - телеграм бот, который может решать цдз тесты\n\n"
                              "***🤝 Сотрудничество:***\n"
                              "Если у вас есть предложение о сотрудничестве, пишите сюда - "
                              "@DRomanovizc", reply_markup=main_menu)
