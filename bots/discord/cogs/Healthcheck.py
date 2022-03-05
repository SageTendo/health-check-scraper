# from discord.ext import cogs
#
# from bots.discord.discordBot import USERS, SESSIONS
# from exceptions.ExceptionHandler import AuthException
# from scraper import HealthCheckAuth
# from scraper.ImageProcessor import ImageProcessor
# from utils.InputHandler import verify_otp
#
#
# class HealthCheck(cogs.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#         self.image_processor = ImageProcessor()
#
#     async def handle_health_check(self, ctx, status_code=0):
#         """
#               TODO: docstring
#
#               :param ctx:
#               :param status_code:
#               :return:
#               """
#
#         auth_id = ctx.author.id
#         if auth_id not in USERS:
#             await ctx.channel.send("ERROR: No user found")
#             return
#
#         auth_session = SESSIONS[auth_id]
#         user = HealthCheckAuth(auth_session)
#
#         try:
#             healthcheck_response = user.generate_health_check(status_code)
#             receipt_type = healthcheck_response['receipt_type']
#             curr_url = healthcheck_response['url']
#             status_div = healthcheck_response['status_div']
#             receipt_div = healthcheck_response['receipt_div']
#
#             await ctx.channel.send('Processing healthcheck receipt.\n'
#                                    'This may take a while...')
#             self.image_processor.generate(user_id=auth_id, status_div=status_div, receipt_div=receipt_div,
#                                           receipt_type=receipt_type)
#             image = self.image_processor.get_image(auth_id)
#             await ctx.channel.send(f'Result: {curr_url}')
#             await ctx.channel.send(file=image)
#         except AuthException as error:
#             await ctx.channel.send(error)
#             await ctx.channel.send("Attempting to log in...")
#             auth_phone = USERS[auth_id]
#             user.login(auth_phone)
#
#             await ctx.channel.send("Waiting For OTP Verification...")
#             msg = await self.bot.wait_for('ctx')
#             try:
#                 verify_otp(msg.content)
#                 user.verify(msg.content)
#                 healthcheck_response = user.generate_health_check(status_code)
#                 curr_url = healthcheck_response['url']
#                 status_div = healthcheck_response['status_div']
#                 receipt_div = healthcheck_response['receipt_div']
#                 receipt_type = healthcheck_response['receipt_type']
#
#                 await ctx.channel.send('Processing healthcheck receipt.\n'
#                                        'This may take a while...')
#                 self.image_processor.generate(user_id=auth_id, status_div=status_div, receipt_div=receipt_div,
#                                               receipt_type=receipt_type)
#                 image = self.image_processor.get_image(auth_id)
#                 await ctx.channel.send(f'Result: {curr_url}')
#                 await ctx.channel.send(file=image)
#             except AuthException as error:
#                 await msg.channel.send(error)
#
#     @cogs.command()
#     async def green(self, ctx):
#         await self.handle_health_check(ctx, 0)
#
#     @cogs.command()
#     async def orange(self, ctx):
#         await self.handle_health_check(ctx, 1)
#
#     @cogs.command()
#     async def red(self, ctx):
#         await self.handle_health_check(ctx, 2)
#
#
# def setup(bot):
#     bot.add_cog(HealthCheck(bot))
#     print("loaded cogs.HealthCheck")
