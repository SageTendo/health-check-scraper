# import os
# import time
#
# from discord.ext import cogs
#
# from bots.setup import load_cogs
# from logger import Logger
#
# from settings import DISCORD_KEY, DISCORD_BOT_OWNER
#
# USERS = {}
# SESSIONS = {}
#
# bot = cogs.Bot(command_prefix='$', help_command=None)
# bot.owner_id = DISCORD_BOT_OWNER
#
#
# @bot.command()
# async def load(ctx, extension):
#     extension = extension.capitalize()
#     bot.load_extension(f'cogs.{extension}')
#     await ctx.send(f'loaded cogs.{extension}')
#
#
# @bot.command()
# async def unload(ctx, extension):
#     extension = extension.capitalize()
#     bot.unload_extension(f'cogs.{extension}')
#     await ctx.send(f'unloaded cogs.{extension}')
#
#
# @bot.command()
# async def reload_all(ctx):
#     print("Reloading Cogs...")
#     await ctx.send("Reloading Cogs...")
#     for filename in os.listdir('./cogs'):
#         if filename.endswith('.py'):
#             bot.unload_extension(f'cogs.{filename[:-3]}')
#             time.sleep(0.5)
#             bot.load_extension(f'cogs.{filename[:-3]}')
#
#
# @bot.command()
# async def reload(ctx, extension):
#     extension = extension.capitalize()
#     bot.unload_extension(f'cogs.{extension}')
#     bot.load_extension(f'cogs.{extension}')
#     await ctx.send(f'reloaded cogs.{extension}')
#
#
# @bot.event
# async def on_ready():
#     print("[BOT] - STARTED")
#
#
# @bot.event
# async def on_message(message):
#     """
#     TODO: docstring
#
#     :return:
#     """
#     if message.author == bot.user:
#         return
#
#     await bot.process_commands(message)
#
#
# if __name__ == '__main__':
#     Logger.debug = True
#     try:
#         load_cogs(bot)
#         bot.run(DISCORD_KEY)
#     except Exception as e:
#         print(e)
