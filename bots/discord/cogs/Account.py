# import os
#
# from discord.ext import commands
# from bots.discord.discordBot import USERS, SESSIONS
# from exceptions.ExceptionHandler import AuthException
# from logger.Logger import DEBUG
# from scraper import HealthCheckAuth
# from settings import static_path
# from utils.InputHandler import verify_phone, verify_otp
#
#
# class Account(commands.Cog):
#     def __init__(self, bot: cogs.Bot):
#         self.bot = bot
#
#     @commands.command()
#     async def setup(self, ctx, auth_phone):
#         """
#         TODO: docstring
#
#         :param auth_phone:
#         :param ctx:
#         """
#         auth_id = ctx.author.id
#
#         try:
#             verify_phone(auth_phone)
#
#             if auth_id not in USERS:
#                 user = HealthCheckAuth()
#                 user.login(auth_phone)
#                 await ctx.send("Waiting For OTP Verification...")
#
#                 msg = await self.bot.wait_for('message')
#                 try:
#                     verify_otp(msg.content)
#                     user.verify(msg.content)
#                     SESSIONS[auth_id] = user.user_session
#                     USERS[auth_id] = auth_phone
#                     DEBUG(f'USERS : {str(USERS)}')
#                     DEBUG(f'USER_SESSIONS : {str(SESSIONS)}')
#                     await ctx.channel.send('SUCCESS: Logged in successfully')
#
#                     # Prompt for vaccine uptake
#                     # vaccine_prompt_text = "Please indicate whether you have been:\n" \
#                     #                       "Fully(**F**)\n" \
#                     #                       "Partially(**P**) or \n" \
#                     #                       "Not(**N**)\n" \
#                     #                       "vaccinated by selecting the corresponding emoji below."
#                     # await ctx.send(vaccine_prompt_text)
#                     # vaccine_uptake = await self.bot.wait_for('message')
#                 except AuthException as error:
#                     await ctx.send(error)
#             else:
#                 await ctx.send('ERROR: User already exists')
#         except IndexError:
#             await ctx.send('ERROR: Phone number not provided')
#             DEBUG(f'USER {ctx.author} did not provide a phone number')
#         except AuthException as error:
#             await ctx.send(error)
#
#     @cogs.command()
#     async def remove(self, ctx):
#         """
#         TODO: docstring
#
#         :param ctx:
#         """
#         auth_id = ctx.author.id
#         if auth_id in USERS:
#
#             user_session = SESSIONS[auth_id]
#             user = HealthCheckAuth(user_session)
#
#             user.close_session()
#             USERS.pop(auth_id)
#             SESSIONS.pop(auth_id)
#
#             try:
#                 os.remove(f'{static_path}/user_receipts/{auth_id}.png')
#             except FileNotFoundError:
#                 pass
#
#             if auth_id not in USERS and auth_id not in SESSIONS:
#                 await ctx.send("SUCCESS: User deleted")
#             else:
#                 await ctx.send("ERROR: Failed to delete user")
#         else:
#             await ctx.send("ERROR: Unauthorised request made")
#
#
# def setup(bot):
#     bot.add_cog(Account(bot))
#     print("loaded cogs.Account")
