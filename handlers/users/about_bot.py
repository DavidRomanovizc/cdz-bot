from keyboards.inline.proj_sup import supported
from aiogram.types import CallbackQuery
from loader import dp


@dp.callback_query_handler(text="about_bot")
async def get_inf_bot(call: CallbackQuery):
    await call.message.edit_text(f"***👑 О боте***\n"
                                 f"Этот бот решает цдз тесты\n"
                                 f"Creator ***@DRomanovizc***", reply_markup=supported)
