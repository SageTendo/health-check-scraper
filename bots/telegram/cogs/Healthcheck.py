import telegrampy
from telegrampy.ext import commands as cogs

from bots.telegram.telegramBot import users, user_sessions
from exceptions.ExceptionHandler import AuthException
from scraper import AccountScraper
from scraper.ImageProcessor import ImageProcessor


class HealthCheck(cogs.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.image_processor = ImageProcessor()

    async def handle_health_check(self, ctx):
        auth_id = ctx.author.id
        if auth_id not in users:
            await ctx.send("ERROR: No user found")
            return

        auth_session = user_sessions[auth_id]
        user = AccountScraper(auth_session)

        try:
            health_status = str(ctx.command).strip()
            healthcheck_response = user.generate_health_check(health_status)
            receipt_type = healthcheck_response['receipt_type']
            # curr_url = healthcheck_response['url']
            status_div = healthcheck_response['status_div']
            receipt_div = healthcheck_response['receipt_div']

            await ctx.send('Processing healthcheck receipt.\n'
                           'This may take a while...')
            self.image_processor.generate_image(user_id=auth_id, status_div=status_div, receipt_div=receipt_div,
                                                receipt_type=receipt_type)
            image = self.image_processor.open_image(auth_id)
            await ctx.send_action('upload_photo')
            telegram_image = telegrampy.Photo(file=image, filename='healthcheck.jpg', caption='Healthcheck Result')
            await ctx.send(file=telegram_image)
        except AuthException as error:
            await ctx.send(error)

    @cogs.command()
    async def green(self, ctx):
        await self.handle_health_check(ctx)

    @cogs.command()
    async def orange(self, ctx):
        await self.handle_health_check(ctx)

    @cogs.command()
    async def red(self, ctx):
        await self.handle_health_check(ctx)


def setup(bot):
    bot.add_cog(HealthCheck(bot))
    print("loaded cogs.HealthCheck")
