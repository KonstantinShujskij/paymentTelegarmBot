import time

from aiogram import types
from aiogram.dispatcher import FSMContext

import utils
from loader import dp
from states.admin.states import set_course_state, report_state, refill_state
from api.requests import admin
from templates import partner_messages, report_message
from excel import create_report


@dp.message_handler(state=set_course_state.course)
async def set_course(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    partner = await state.get_data('partner')
    partner_id = partner['id']

    try:
        value = float(message.text)
        partner = admin.set_course(partner_id, value)
    except Exception as error:
        await dp.bot.send_message(chat_id=user_id, text=error)
        return

    await dp.bot.send_message(chat_id=user_id, **partner_messages.update_course(partner))

    await state.update_data(value=value)
    await state.finish()


@dp.message_handler(state=report_state.start_date)
async def set_course(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    value = message.text

    start_time = 0

    try:
        if not value.lower() == 'all':
            start_time = utils.parse_time(value)

    except Exception as error:
        await dp.bot.send_message(chat_id=user_id, text=error)
        return

    await state.update_data(value=start_time)
    await report_state.stop_date.set()

    await message.answer(**report_message.get_stop_date())


@dp.message_handler(state=report_state.stop_date)
async def set_course(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    value = message.text
    stop_time = int(time.time() * 1000)

    start_date = await state.get_data('start_date')
    start_time = start_date['value']

    partner = await state.get_data('partner')
    partner_id = partner['id']

    await state.finish()

    try:
        if not value.lower() == 'now':
            stop_time = utils.parse_time(value)

        orders = admin.get_orders(start_time, stop_time, partner_id)
    except Exception as error:
        await dp.bot.send_message(chat_id=user_id, text=error)
        return

    loader_message = await dp.bot.send_message(chat_id=user_id, text='Пожалуйста подождите')

    document = create_report(orders, 'report')

    await dp.bot.send_document(chat_id=user_id, document=document)
    await loader_message.delete()


@dp.message_handler(state=refill_state.value)
async def refill(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    maker = await state.get_data('maker')
    maker_id = maker['id']
    currency = (await state.get_data('currency'))['currency']

    await state.finish()

    try:
        value = float(message.text)
        admin.refill(maker_id, value, currency)
    except Exception as error:
        await dp.bot.send_message(chat_id=user_id, text=error)
        return

    await message.answer(text='balance has refill')