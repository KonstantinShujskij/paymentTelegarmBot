from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from templates import MessageData


def get_start_date():
    text = f"Введите дату начала отчета::\n" \
           f"( формат dd.mm.yyyy )\n" \
           f"Укажите 'all' что бы выбрать все до даты окончния"

    return MessageData(text).__dict__


def get_stop_date():
    text = f"Введите дату конца отчета:\n" \
           f"( формат dd.mm.yyyy )\n" \
           f"Дата не будет включена в отчет!\n" \
           f"Укажите 'now' что бы включить все до текущего времени"

    return MessageData(text).__dict__
