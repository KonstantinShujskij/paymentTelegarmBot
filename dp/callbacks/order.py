from aiogram import types
from loader import dp
from dp.callbacks.objects import order as Callback
from templates import order_messages as Messages

from controllers import get_taker
from api.requests import order as Order


@dp.callback_query_handler(Callback.filter(action='take'))
async def take_callback(callback: types.CallbackQuery, callback_data: dict):
    order_id = callback_data['id']
    user_id = callback.from_user.id
    user_name = callback.from_user.username

    try:
        taker = get_taker(user_id)
        order = Order.take(order_id, taker.id)
    except Exception as error:
        await callback.message.answer(text=str(error))
        return

    await callback.message.edit_text(**Messages.work_order(order, user_name))
    await dp.bot.send_message(chat_id=user_id, **Messages.wait_order(order, callback.message))


@dp.callback_query_handler(Callback.filter(action='confirm'))
async def confirm_callback(callback: types.CallbackQuery, callback_data: dict):
    chat_id = callback_data['chat']
    message_id = callback_data['message']
    order_id = callback_data['id']
    user_name = callback.from_user.username

    try:
        order = Order.confirm(order_id)
    except Exception as error:
        await callback.message.delete()
        await callback.message.answer(text=str(error))
        return

    await callback.message.edit_text(**Messages.wait_order(order, None))
    await dp.bot.edit_message_text(**Messages.work_order(order, user_name), chat_id=chat_id, message_id=message_id)


@dp.callback_query_handler(Callback.filter(action='reject'))
async def reject_callback(callback: types.CallbackQuery, callback_data: dict):
    chat_id = callback_data['chat']
    message_id = callback_data['message']
    order_id = callback_data['id']
    user_name = callback.from_user.username

    try:
        order = Order.reject(order_id)
    except Exception as error:
        await callback.message.delete()
        await callback.message.answer(text=str(error))
        return

    await callback.message.edit_text(**Messages.wait_order(order, None))
    await dp.bot.edit_message_text(**Messages.work_order(order, user_name), chat_id=chat_id, message_id=message_id)


