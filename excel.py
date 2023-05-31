import pandas as pd

from utils import parse_date


def create_report(orders, file_name):
    data = {
        'id': [],
        'value': [],
        'card': [],
        'course': [],
        'currency': [],
        'status': [],
        'maker': [],
        'taker': [],
        'partner': [],
        'create': [],
        'update': []
    }

    for order in orders:
        data['id'].append(order.id)
        data['value'].append(order.value)
        data['card'].append(order.card),
        data['course'].append(order.course),
        data['currency'].append(order.currency),
        data['status'].append(order.status),
        data['maker'].append(order.maker),
        data['taker'].append(order.taker)
        data['partner'].append(order.partner),
        data['create'].append(parse_date(order.create)),
        data['update'].append(parse_date(order.update)),

    df = pd.DataFrame({
        'Id': data['id'],
        'Value': data['value'],
        'Card': data['card'],
        'Course': data['course'],
        'Currency': data['currency'],
        'Status': data['status'],
        'Maker': data['maker'],
        'Taker': data['taker'],
        'Partner': data['partner'],
        'Create': data['create'],
        'Update': data['update']
    })

    df.to_excel(f"./{file_name}.xlsx")

    return open(f"./{file_name}.xlsx", 'rb')
