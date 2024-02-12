import logging

from telegrampy.ext import commands as cogs

from bots.setup import load_cogs
from settings import TELEGRAM_KEY, telegram_bot_path, TELEGRAM_BOT_OWNER

users = {}
user_sessions = {}
vaccine_uptakes = {}

bot: cogs.Bot = cogs.Bot(token=TELEGRAM_KEY, owner_id=TELEGRAM_BOT_OWNER)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    try:
        load_cogs(telegram_bot_path, bot)
        print("[BOT] - STARTED")
        bot.run()
    except Exception as e:
        print(e)
