from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dp.callbacks.objects import maker as Callback

from templates import MessageData


def data(user):
    usdt = round(float(user.balance['usdt']), 2)
    uah = round(float(user.balance['uah']), 2)

    usdt_recive = round(float(user.recive['usdt']), 2)
    uah_recive = round(float(user.recive['uah']), 2)

    text = f"Id: {user.id}\n" \
           f"Пользователь: {user.name}\n" \
           f"Баланс:\n" \
           f"USDT: {usdt}\n" \
           f"UAH: {uah}\n" \
           f"Заблокированный баланс:\n" \
           f"USDT: {usdt_recive}\n" \
           f"UAH: {uah_recive}"

    keyboard = InlineKeyboardMarkup(row_width=2)

    refill_callback = Callback.new(action="refill-usdt", id=user.id)
    keyboard.add(InlineKeyboardButton(text='Пополнить USDT', callback_data=refill_callback))

    refill_callback = Callback.new(action="refill-uah", id=user.id)
    keyboard.add(InlineKeyboardButton(text='Пополнить UAH', callback_data=refill_callback))

    return MessageData(text, keyboard).__dict__
