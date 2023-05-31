import requests
import hashlib
import hmac
import json

from data import config


def generate_signature(body, private_token):
    request = json.dumps(body, separators=(',', ':'))
    requestBytes = bytes(request, 'utf-8')
    privateTokenBytes = bytes(private_token, 'utf-8')

    signature = hmac.new(privateTokenBytes, requestBytes, digestmod=hashlib.sha256).hexdigest()

    return signature


def send_request(url, body=None, access_token=config.ACCESS_TOKEN, private_token=config.PRIVATE_TOKEN):
    if body is None:
        body = {}

    body['accessToken'] = access_token
    body['signature'] = generate_signature(body, private_token)

    try:
        res = requests.post(url, json=body)
        res = res.json()
    except:
        raise Exception('Somthing went wrong')

    if 'error' in res:
        raise Exception(res['error'])

    return res


def send_admin_request(url, body=None):
    return send_request(url, body,
                        access_token=config.ADMIN_ACCESS_TOKEN,
                        private_token=config.ADMIN_PRIVATE_TOKEN)
