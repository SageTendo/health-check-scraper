from telegrampy.ext import commands as cogs

from bots.setup import load_cogs
from logger import Logger

from settings import TELEGRAM_KEY, telegram_bot_path

users = {}
user_sessions = {}
vaccine_uptakes = {}

bot: cogs.Bot = cogs.Bot(token=TELEGRAM_KEY, owner_id=2008369677)


# @bot.event
# async def on_command_error(ctx, error):
#     """
#
#     :param ctx:
#     :param error:
#     """
#     await ctx.reply(error)
#     print(error)


if __name__ == '__main__':
    Logger.debug = True
    try:
        load_cogs(telegram_bot_path, bot)
        print("[BOT] - STARTED")
        bot.run()
    except Exception as e:
        print(e)
