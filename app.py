import sys

from data import config
from loader import bot
from api.requests import subscribe


async def on_startup(dp):
    try:
        subscribe.on()
        await bot.set_webhook(config.WEBHOOK_URL)
    except:
        sys.exit('API Not Connection')


async def on_shutdown(dp):
    await bot.delete_webhook()


if __name__ == '__main__':
    from start_webhook import start_webhook
    from dp import dp

    start_webhook(
        dispatcher=dp,
        webhook_path=config.WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT
    )