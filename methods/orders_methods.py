import requests

import data


class OrderMethods:

    @staticmethod
    def create_order(ingredients, headers=None):
        response = requests.post(f'{data.BASE_URL}{data.ORDERS_URL}', json={
"ingredients": ingredients
}, headers=headers)
        return response.status_code, response.json()

    @staticmethod
    def get_orders(token):
        response = requests.get(f'{data.BASE_URL}{data.ORDERS_URL}', headers={'Authorization': token})
        return response.status_code, response.json()