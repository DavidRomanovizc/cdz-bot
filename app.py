import logging
from aiogram import executor

from loader import dp, db, bot, storage
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    import filters
    import middlewares

    await db.create()
    await db.create_table_users()
    from utils.notify_admins import on_startup_notify

    await on_startup_notify(dp)
    await set_default_commands(dp)


async def on_shutdown():
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)