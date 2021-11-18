from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

supported = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="💸 Подписка", callback_data="donation"),
                                         InlineKeyboardButton(text="🆘 Контакт поддержки",
                                                              url="https://t.me/DRomanovizc")
                                     ],
                                     [
                                         InlineKeyboardButton(text="🔙 Назад", callback_data="back")
                                     ]
                                 ])
