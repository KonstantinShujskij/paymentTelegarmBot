from api.request import send_request
from utils import Struct
from data import config


def create(name):
    end_point = '/api/taker/create'
    url = config.API_URL + end_point

    body = {'name': name}

    data = send_request(url, body)
    taker = Struct(**data)
    return taker


def find(name):
    end_point = '/api/taker/find'
    url = config.API_URL + end_point

    body = {'name': name}

    data = send_request(url, body)
    taker = Struct(**data)
    return taker