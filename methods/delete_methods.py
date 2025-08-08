import allure
import requests

import data


class DeleteMethods:

    @staticmethod
    @allure.step('Удаление юзера')
    def delete_user():
        requests.delete(f'{data.BASE_URL}/auth{data.USER_URL}')