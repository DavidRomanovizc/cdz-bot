from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(row_width=4,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="🤖 О боте", callback_data="about_bot"),
                                         InlineKeyboardButton(text="📗 Руководство", callback_data="guide_btn")
                                     ],
                                     [

                                         InlineKeyboardButton(text="📈 Статистика", callback_data="stats")

                                     ],
                                     [
                                         InlineKeyboardButton(text="💻 ‍Решить тест", callback_data="pass_test")
                                     ],
                                     [
                                         InlineKeyboardButton(text="💸 Приобрести подписку", callback_data="pay_balance")
                                     ]
                                 ])
