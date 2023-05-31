from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dp.callbacks.objects import partner as Callback

from templates import MessageData


def data(partner):
    text = f"Id: <code>{partner.id}</code>\n" \
           f"Партнер: {partner.name}\n" \
           f"Курс: {partner.course}"

    keyboard = InlineKeyboardMarkup(row_width=2)

    set_course_callback = Callback.new(action="set-course", id=partner.id)
    keyboard.add(InlineKeyboardButton(text='Установить курс', callback_data=set_course_callback))

    report_callback = Callback.new(action="report", id=partner.id)
    keyboard.add(InlineKeyboardButton(text='Сформировать отчет', callback_data=report_callback))

    makers_callback = Callback.new(action="makers", id=partner.id)
    keyboard.add(InlineKeyboardButton(text='Список пользователей', callback_data=makers_callback))

    return MessageData(text, keyboard).__dict__


def update_course(partner):
    text = f"Для {partner.name} установлен курс {partner.course}"

    return MessageData(text).__dict__
