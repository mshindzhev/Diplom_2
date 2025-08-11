import allure
import requests

import data


class OrderMethods:

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(ingredients, headers=None):
        response = requests.post(f'{data.BASE_URL}{data.ORDERS_URL}', json={
"ingredients": ingredients
}, headers=headers)
        return response.status_code, response.json()

    @staticmethod
    @allure.step('Получение заказов пользователя')
    def get_orders(token):
        response = requests.get(f'{data.BASE_URL}{data.ORDERS_URL}', headers={'Authorization': token})
        return response.status_code, response.json()