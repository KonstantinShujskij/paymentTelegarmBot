import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

ADMIN_ACCESS_TOKEN = str(os.getenv('ADMIN_ACCESS_TOKEN'))
ADMIN_PRIVATE_TOKEN = str(os.getenv('ADMIN_PRIVATE_TOKEN'))

ACCESS_TOKEN = str(os.getenv('ACCESS_TOKEN'))
PRIVATE_TOKEN = str(os.getenv('PRIVATE_TOKEN'))

API_URL = str(os.getenv('API_URL'))
CALLBACK_ENDPOINT = str(os.getenv('CALLBACK_URL'))

WEBAPP_HOST = str(os.getenv('WEBAPP_HOST'))
WEBAPP_PORT = int(os.getenv('WEBAPP_PORT'))
WEBHOOK_HOST = str(os.getenv('WEBHOOK_HOST'))

WEBHOOK_PATH = f"{CALLBACK_ENDPOINT}/{BOT_TOKEN}/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

CALLBACK_URL = f"{WEBHOOK_HOST}{CALLBACK_ENDPOINT}"

# Telegram Settings

admins_id = [
    253079275
]

moderators_id = [
    253079275
]

work_group = -943481444
