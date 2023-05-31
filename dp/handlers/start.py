from aiogram import types
from loader import dp
from utils import end_dialog


@dp.message_handler(text='/start')
async def command_start(message: types.message):
    return await end_dialog(message, 'Бот запущен')




