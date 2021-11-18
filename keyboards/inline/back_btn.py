from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back_to_menu = InlineKeyboardMarkup(row_width=1,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text="🔙 Назад", callback_data="back")
                                        ]
                                    ])
