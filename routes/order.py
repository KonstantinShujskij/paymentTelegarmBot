from aiohttp import web
from api.requests import order as Order
from templates.order_messages import new_order
from loader import bot
from data.config import work_group


async def create_handler(request):
    data = await request.json()
    order_id = data['id']
    order = Order.get(order_id)

    await bot.send_message(work_group, **new_order(order))

    return web.Response(text="ok")


routes = [
    web.post('/api/order/create', create_handler),
]