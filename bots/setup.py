import os


def load_cogs(path, bot):
    for filename in os.listdir(f'{path}/cogs'):
        if not filename.startswith("__init__.py"):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')


def unload_cogs(bot):
    for cog in bot.cogs:
        bot.unload_extension(cog)
