from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types
from api.requests import admin
from templates import partner_messages, report_message
from states.admin.states import report_state
from data import config
import check


@dp.message_handler(text='/set_work_group')
async def command_start(message: types.message):
    chat_id = message.chat.id

    try:
        check.is_admin(message.from_user.id)
    except Exception as error:
        await message.answer(text=error)
        await message.delete()
        return

    config.work_group = chat_id

    await message.answer(text=f"Its group has set a work group. id - {chat_id}")
    await message.delete()


@dp.message_handler(text='/partners')
async def get_partners(message: types.message):
    print('lox')

    try:
        check.is_private(message)
        check.is_moderator(message.from_user.id)
        partners = admin.get_partners()
    except Exception as error:
        await message.answer(text=error)
        await message.delete()
        return

    for partner in partners:
        await message.answer(**partner_messages.data(partner))

    await message.delete()


@dp.message_handler(text='/orders')
async def get_orders(message: types.message, state: FSMContext):
    try:
        check.is_private(message)
        check.is_moderator(message.from_user.id)
    except Exception as error:
        await message.answer(text=error)
        await message.delete()
        return

    await report_state.partner.set()
    await state.update_data(id=False)
    await report_state.start_date.set()

    await message.answer(**report_message.get_start_date())
    await message.delete()
