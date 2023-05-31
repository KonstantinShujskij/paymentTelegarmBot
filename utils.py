import datetime


class Struct:
    def __init__(self, **properties):
        self.__dict__.update(properties)

    def __str__(self):
        return self.__dict__.__str__()


async def end_dialog(message, answer):
    await message.answer(text=answer)
    await message.delete()

    return None


def parse_time(date):
    return int(datetime.datetime.strptime(date, '%d.%m.%Y').timestamp() * 1000)


def parse_date(millis):
    return datetime.datetime.fromtimestamp(millis / 1000.0).strftime("%m/%d/%Y, %H:%M:%S")