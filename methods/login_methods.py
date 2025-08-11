import allure
import requests

import data


class LoginMethods:

    @staticmethod
    @allure.step('Логин юзера')
    def user_login(email, password):
        response = requests.post(f'{data.BASE_URL}/auth{data.LOGIN_URL}', json={"email": email, "password": password})
        return response.status_code, response.json()