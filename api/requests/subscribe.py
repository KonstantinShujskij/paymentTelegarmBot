from api.request import send_request
from data import config


def on():
    end_point = '/api/subscribe/on'
    url = config.API_URL + end_point

    body = {'url': config.CALLBACK_URL}

    send_request(url, body)

