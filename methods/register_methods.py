import allure
import requests

import data
from helpers import generate_data_for_registration


class RegisterMethods:

    @staticmethod
    @allure.step('Регистрация юзера')
    def user_registration(email=None, password=None, name=None, need_generate_data=True):
        response = requests.post(f'{data.BASE_URL}/auth{data.REGISTER_URL}', data={
    "email": email,
    "password": password,
    "name": name
})
        if need_generate_data:
            response = requests.post(f'{data.BASE_URL}/auth{data.REGISTER_URL}', data=generate_data_for_registration())
        return response.status_code, response.json()

