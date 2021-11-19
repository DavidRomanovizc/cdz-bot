from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice_payment = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text="ЮKassa", callback_data="ykassa_pay")
                                          ],
                                          [
                                              InlineKeyboardButton(text="Назад", callback_data="cancel")
                                          ]
                                      ])