from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

pay_Qiwi = InlineKeyboardMarkup(row_width=4,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="💳 Qiwi", callback_data="pay_qiwi"),
                                        InlineKeyboardButton(text="🔄 Проверить цены", callback_data="check_price"),

                                    ],
                                    [
                                        InlineKeyboardButton(text="🆘 Контакт поддержки",
                                                             url="https://t.me/DRomanovizc")
                                    ],
                                    [
                                        InlineKeyboardButton(text="🔙 Назад", callback_data="back")
                                    ]

                                ])

buy_sub = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text="💸 Приобрести подписку", callback_data="pay_balance")
                                   ]
                               ])
