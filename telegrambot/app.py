import asyncio
from aiogram.utils.executor import start_webhook
import logging
from loader import dp, bot
import middlewares
import filters
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from data.config import WEBHOOK_PATH, WEBHOOK_URL, WEBAPP_PORT, WEBAPP_HOST


async def on_startup(dispatcher):
    webhook = await bot.get_webhook_info()
    if webhook.url != WEBHOOK_URL:
        if not webhook.url:
            await bot.delete_webhook()
        await bot.set_webhook(WEBHOOK_URL)
    await asyncio.gather(set_default_commands(dispatcher), on_startup_notify(dispatcher))


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await asyncio.gather(bot.delete_webhook(),
                         dp.storage.close(),
                         dp.storage.wait_closed())
    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )

