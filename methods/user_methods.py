import allure
import requests

import data


class UserMethods:

    @staticmethod
    @allure.step('Удаление юзера')
    def delete_user(token):
        response = requests.delete(f'{data.BASE_URL}/auth{data.USER_URL}', headers={'Authorization': token})
        return response.status_code, response.json()

    @staticmethod
    @allure.step('Изменение данных юзера')
    def edit_user(token, new_data):
        response = requests.patch(f'{data.BASE_URL}/auth{data.USER_URL}', headers={'Authorization': token}, json=new_data)
        return response.status_code, response.json()

    @staticmethod
    @allure.step('Получение данных юзера')
    def get_user(token):
        response = requests.get(f'{data.BASE_URL}/auth{data.USER_URL}', headers={'Authorization': token})
        return response.status_code, response.json()