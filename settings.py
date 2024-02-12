from dotenv import load_dotenv, find_dotenv
import os

# ENVIRONMENT VARIABLE SETUP
load_dotenv(find_dotenv())
DISCORD_KEY = os.environ.get("DISCORD_KEY")
DISCORD_BOT_OWNER = os.environ.get("DISCORD_BOT_OWNER")
TELEGRAM_KEY = os.environ.get("TELEGRAM_KEY")
TELEGRAM_BOT_OWNER = os.environ.get("TELEGRAM_BOT_OWNER")

# FILE PATHS
root_path = os.path.dirname(__file__)
discord_bot_path = os.path.join(root_path, 'bots/discord')
telegram_bot_path = os.path.join(root_path, 'bots/telegram')
static_path = os.path.join(root_path, 'static')
css_path = os.path.join(static_path, 'css')
images_path = os.path.join(static_path, 'images')
user_receipts_path = os.path.join(static_path, 'user_receipts')
