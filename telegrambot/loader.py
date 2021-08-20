from aiogram import Bot, Dispatcher, types
from data import config
from aiogram.contrib.fsm_storage.files import MemoryStorage
import asyncio
import logging
import uvloop

loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)
logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(config.API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, loop=loop, storage=storage)

