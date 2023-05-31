from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dp.callbacks.objects import order as Callback
from templates import MessageData
from utils import parse_date


status_icon = {
    'CREATE': '🆕',
    'WAIT': '🔁',
    'CONFIRM': '✅',
    'REJECT': '❌'
}


def new_order(order):
    time_create = parse_date(order.create)
    card = order.card.replace(' ', '')
    card = card[:6] + "<span class='tg-spoiler'>******</span>" + card[12:]

    text = f"🆕\n" \
           f"Id: <code>{order.id}</code>\n" \
           f"Банк: не известно\n" \
           f"Сумма: {order.value} ₴\n" \
           f"Карта: {card}\n" \
           f"Статус: {order.status}\n" \
           f"Создан: {time_create}" \

    keyboard = InlineKeyboardMarkup(row_width=2)

    take_callback = Callback.new(action="take", id=order.id, chat=0, message=0)
    keyboard.add(InlineKeyboardButton(text='Взять в работу', callback_data=take_callback))

    return MessageData(text, keyboard).__dict__


def work_order(order, taker):
    time_create = parse_date(order.create)
    time_update = parse_date(order.update)

    card = order.card.replace(' ', '')
    card = card[:6] + "<span class='tg-spoiler'>******</span>" + card[12:]

    text = f"{status_icon[order.status]}\n" \
           f"Id: <code>{order.id}</code>\n" \
           f"Банк: не известно\n" \
           f"Сумма: {order.value} ₴\n" \
           f"Карта: {card}\n" \
           f"Статус: {order.status}\n" \
           f"Оператор: @{taker}\n" \
           f"Создан: {time_create}\n" \
           f"Обновлен: {time_update}" \

    return MessageData(text).__dict__


def wait_order(order, message):
    card = order.card.replace(' ', '')

    text = f"{status_icon[order.status]}\n" \
           f"Id: <code>{order.id}</code>\n" \
           f"Банк: не известно\n" \
           f"Сумма: {order.value} ₴\n" \
           f"Карта: <code>{card}</code>\n" \
           f"Статус: {order.status}\n"

    keyboard = None

    if order.status == 'WAIT':
        keyboard = InlineKeyboardMarkup(row_width=2)

        confirm_callback = Callback.new(
            action="confirm",
            id=order.id,
            chat=message.chat.id,
            message=message.message_id
        )
        keyboard.add(InlineKeyboardButton(text='Подтвердить выполнение', callback_data=confirm_callback))

        reject_callback = Callback.new(
            action="reject",
            id=order.id,
            chat=message.chat.id,
            message=message.message_id
        )
        keyboard.add(InlineKeyboardButton(text='Отклонить ордер', callback_data=reject_callback))

    return MessageData(text, keyboard).__dict__
