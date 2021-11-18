from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(row_width=4,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="🤖 О боте", callback_data="about_bot"),
                                         InlineKeyboardButton(text="📰 Информация", callback_data="information")
                                     ],
                                     [
                                         InlineKeyboardButton(text="💻 ‍Решить тест", callback_data="pass_test")
                                     ],
                                     [
                                         InlineKeyboardButton(text="📈 Статистика", callback_data="stats")
                                     ]
                                 ])