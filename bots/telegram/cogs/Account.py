import os

from telegrampy.ext import commands as cogs

from bots.telegram.telegramBot import users, user_sessions, vaccine_uptakes
from exceptions.ExceptionHandler import AuthException
from logger.Logger import DEBUG
from scraper import AccountScraper
from settings import static_path
from utils.InputHandler import verify_phone, verify_otp


class Account(cogs.Cog):
    def __init__(self, bot: cogs.Bot):
        self.bot = bot

    @cogs.command()
    async def setup(self, ctx, phone_number):
        """
        TODO: docstring

        :param phone_number:
        :param ctx:
        """
        auth_id = ctx.author.id

        try:
            verify_phone(phone_number)

            if auth_id not in users:
                user = AccountScraper()
                user.login(phone_number)
                await ctx.reply("Waiting For OTP Verification...")

                otp_msg = await self.bot.wait_for('message')
                try:
                    verify_otp(otp_msg.content)
                    user.verify_login(otp_msg.content)

                    # Prompt for vaccine uptake
                    # FULLY, PARTIALLY, NOT
                    vaccine_prompt_text = "Please indicate whether you have been:\n" \
                                          "<strong>F</strong>: <em>Fully Vaccinated</em>\n" \
                                          "<strong>P</strong>: <em>Partially Vaccinated</em>\n" \
                                          "<strong>N</strong>: <em>Not Vaccinated</em>\n"

                    await ctx.send(vaccine_prompt_text, parse_mode='HTML')
                    vaccine_uptake_msg = await self.bot.wait_for('message')

                    user_sessions[auth_id] = user.get_session()
                    users[auth_id] = phone_number
                    vaccine_uptakes[auth_id] = vaccine_uptake_msg.content
                    DEBUG(f'USERS : {str(users)}')
                    DEBUG(f'USER_SESSIONS : {str(user_sessions)}')
                    await ctx.send('SUCCESS: Logged in successfully')
                except AuthException as error:
                    await ctx.send(error)
            else:
                await ctx.send('ERROR: User already exists')
        except IndexError:
            await ctx.send('ERROR: Phone number not provided')
            DEBUG(f'USER {ctx.author} did not provide a phone number')
        except AuthException as error:
            await ctx.send(error)

    @cogs.command()
    async def remove(self, ctx):
        """
        TODO: docstring

        :param ctx:
        """
        auth_id = ctx.author.id
        if auth_id in users:

            user_session = user_sessions[auth_id]
            user = AccountScraper(user_session)

            user.close_session()
            users.pop(auth_id)
            user_sessions.pop(auth_id)

            try:
                os.remove(f'{static_path}/user_receipts/{auth_id}.png')
            except FileNotFoundError:
                pass

            if auth_id not in users and auth_id not in user_sessions:
                await ctx.send("SUCCESS: User deleted")
            else:
                await ctx.send("ERROR: Failed to delete user")
        else:
            await ctx.send("ERROR: Unauthorised request made")


def setup(bot):
    bot.add_cog(Account(bot))
    print("loaded cogs.Account")
