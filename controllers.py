from api.requests import taker as Taker


def get_taker(name):
    try:
        taker = Taker.find(name)
    except Exception as error:
        if str(error) == 'User Not Exist':
            taker = Taker.create(name)
        else:
            raise error

    return taker
