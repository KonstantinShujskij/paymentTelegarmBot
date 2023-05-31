from api.request import send_request
from utils import Struct
from data import config


def get(order_id):
    end_point = '/api/order/get'
    url = config.API_URL + end_point

    body = {'id': order_id}

    data = send_request(url, body)
    order = Struct(**data)

    return order


def list():
    end_point = '/api/order/list'
    url = config.API_URL + end_point

    data = send_request(url)
    orders = []
    for order in data:
        orders.append(Struct(**order))

    return orders


def take(order_id, taker_id):
    end_point = '/api/order/take'
    url = config.API_URL + end_point

    body = {'taker': taker_id, 'order': order_id}

    data = send_request(url, body)
    order = Struct(**data)

    return order


def confirm(order_id):
    end_point = '/api/order/confirm'
    url = config.API_URL + end_point

    body = {'order': order_id}

    data = send_request(url, body)
    order = Struct(**data)

    return order


def reject(order_id):
    end_point = '/api/order/reject'
    url = config.API_URL + end_point

    body = {'order': order_id}

    data = send_request(url, body)
    order = Struct(**data)

    return order
