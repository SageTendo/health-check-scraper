import os

from telegrampy.ext import commands as cogs

is_hidden = True


class Admin(cogs.Cog):
    def __init__(self, bot: cogs.Bot):
        self.bot = bot

    @cogs.is_owner()
    @cogs.command(hidden=is_hidden)
    async def unload(self, ctx, extension):
        extension = extension.capitalize()
        self.bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'unloaded cogs.{extension}')

    @cogs.is_owner()
    @cogs.command(hidden=is_hidden)
    async def load(self, ctx, extension):
        extension = extension.capitalize()
        self.bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'loaded cogs.{extension}')

    @cogs.is_owner()
    @cogs.command(hidden=is_hidden)
    async def reload_all(self, ctx):
        print("Reloading Cogs...")
        await ctx.send("Reloading Cogs...")
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                self.bot.reload_extension(f'cogs.{filename[:-3]}')

    @cogs.is_owner()
    @cogs.command(hidden=is_hidden)
    async def reload(self, ctx, extension):
        extension = extension.capitalize()
        self.bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f'reloaded cogs.{extension}')

    @cogs.is_owner()
    @cogs.command(hidden=is_hidden)
    async def ping(self, ctx):
        await ctx.send("pong!")


def setup(bot):
    bot.add_cog(Admin(bot))
    print(f'loaded cogs.Bot')
