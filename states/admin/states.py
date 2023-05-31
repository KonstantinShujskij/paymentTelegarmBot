from aiogram.dispatcher.filters.state import StatesGroup, State


class set_course_state(StatesGroup):
    course = State()
    partner = State()


class report_state(StatesGroup):
    partner = State()
    start_date = State()
    stop_date = State()


class refill_state(StatesGroup):
    maker = State()
    value = State()
    currency = State()
