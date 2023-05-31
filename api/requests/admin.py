from api.request import send_admin_request
from utils import Struct
from data import config


def get_partners():
    end_point = '/api/admin/get-partners'
    url = config.API_URL + end_point

    data = send_admin_request(url)
    partners = []

    for partner in data:
        partners.append(Struct(**partner))

    return partners


def set_course(partner_id, value):
    end_point = '/api/admin/set-course'
    url = config.API_URL + end_point

    body = {'id': partner_id, 'value': value }

    data = send_admin_request(url, body)
    partner = Struct(**data)

    return partner


def get_orders(start, stop, partner_id):
    end_point = '/api/admin/get-orders'
    url = config.API_URL + end_point

    body = {'timeStart': start, 'timeStop': stop, 'partner': partner_id}

    data = send_admin_request(url, body)
    orders = []

    for order in data:
        orders.append(Struct(**order))

    return orders


def get_makers(partner_id):
    end_point = '/api/admin/get-makers'
    url = config.API_URL + end_point

    body = {'partner': partner_id}

    data = send_admin_request(url, body)
    makers = []

    for maker in data:
        makers.append(Struct(**maker))

    return makers


def refill(maker_id, value, currency):
    end_point = '/api/admin/refill'
    url = config.API_URL + end_point

    body = {'id': maker_id, 'value': {f'{currency}': str(value)}}

    send_admin_request(url, body)

