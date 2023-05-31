from aiogram.utils.executor import set_webhook, DEFAULT_ROUTE_NAME
from routes import routes


def start_webhook(dispatcher, webhook_path, *, loop=None, skip_updates=None,
                  on_startup=None, on_shutdown=None, check_ip=False, retry_after=None,
                  route_name=DEFAULT_ROUTE_NAME, routes=routes,
                  **kwargs):
    executor = set_webhook(dispatcher=dispatcher,
                           webhook_path=webhook_path,
                           loop=loop,
                           skip_updates=skip_updates,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown,
                           check_ip=check_ip,
                           retry_after=retry_after,
                           route_name=route_name)

    app = executor.web_app()
    app.add_routes(routes)

    executor.run_app(**kwargs)