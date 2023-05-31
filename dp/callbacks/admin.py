from aiogram import types
from aiogram.dispatcher import FSMContext


from loader import dp
from dp.callbacks.objects import partner as Callback
from dp.callbacks.objects import maker as makerCallback
from states.admin.states import set_course_state, report_state, refill_state
from api.requests import admin
from templates import user_messages, report_message
import check
from utils import end_dialog


@dp.callback_query_handler(Callback.filter(action='set-course'))
async def set_course_callback(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = callback.from_user.id
    partner_id = callback_data['id']

    await set_course_state.partner.set()
    await state.update_data(id=partner_id)
    await set_course_state.course.set()

    await dp.bot.send_message(chat_id=user_id, text='Установить новый курс:')


@dp.callback_query_handler(Callback.filter(action='report'))
async def report_callback(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = callback.from_user.id
    partner_id = callback_data['id']

    await report_state.partner.set()
    await state.update_data(id=partner_id)
    await report_state.start_date.set()

    await dp.bot.send_message(chat_id=user_id, **report_message.get_start_date())


@dp.callback_query_handler(Callback.filter(action='makers'))
async def get_makers(callback: types.CallbackQuery, callback_data: dict):
    user_id = callback.from_user.id
    partner_id = callback_data['id']

    try:
        makers = admin.get_makers(partner_id)
    except Exception as error:
        await callback.message.answer(text=str(error))
        return

    for maker in makers:
        await dp.bot.send_message(chat_id=user_id, **user_messages.data(maker))


@dp.callback_query_handler(makerCallback.filter(action='refill-usdt'))
async def get_makers(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = callback.from_user.id

    try:
        check.is_admin(user_id)
    except Exception as error:
        return await end_dialog(callback.message, str(error))

    user_id = callback.from_user.id
    maker_id = callback_data['id']

    await refill_state.maker.set()
    await state.update_data(id=maker_id)
    await refill_state.currency.set()
    await state.update_data(currency='usdt')
    await refill_state.value.set()

    await dp.bot.send_message(chat_id=user_id, text="Введите сумму пополнения в USDT:")


@dp.callback_query_handler(makerCallback.filter(action='refill-uah'))
async def get_makers(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = callback.from_user.id

    try:
        check.is_admin(user_id)
    except Exception as error:
        return await end_dialog(callback.message, str(error))

    user_id = callback.from_user.id
    maker_id = callback_data['id']

    await refill_state.maker.set()
    await state.update_data(id=maker_id)
    await refill_state.currency.set()
    await state.update_data(currency='uah')
    await refill_state.value.set()

    await dp.bot.send_message(chat_id=user_id, text="Введите сумму пополнения в UAH:")


