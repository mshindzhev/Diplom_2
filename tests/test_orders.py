import allure
import pytest

import data
from methods.orders_methods import OrderMethods


class TestOrder:

    @pytest.mark.parametrize(
        'ingredients',
        [
            [],
            ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]
        ]
    )
    @allure.title('Создание заказа с невалидными данными')
    def test_create_order_with_invalid_ingredients(self, ingredients):
        order = OrderMethods.create_order(ingredients)
        assert order[0] == 400 and order[1]['success'] == False

    @allure.title('Создание заказа с валидными данными и авторизацией')
    def test_create_order_with_authorization_and_valid_ingredients(self, create_user):
        order = OrderMethods.create_order(data.INGREDIENTS, headers={'Authorization': create_user[1]['accessToken']})
        assert order[0] == 200 and order[1]['success'] == True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorization(self):
        order = OrderMethods.create_order(data.INGREDIENTS)
        assert order[0] == 200 and order[1]['success'] == True

    @allure.title('Получение данных заказа без авторизации')
    def test_get_orders_without_authorization(self):
        orders = OrderMethods.get_orders(None)
        assert orders[0] == 401 and orders[1]['success'] == False

    @allure.title('Получение данных заказа с авторизацией')
    def test_get_orders_with_authorization(self, create_user):
        orders = OrderMethods.get_orders(create_user[1]['accessToken'])
        assert orders[0] == 200 and orders[1]['success'] == True and "orders" in orders[1]

