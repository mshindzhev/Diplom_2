import allure
import pytest

import data
from methods.register_methods import RegisterMethods


class TestRegister:

    @allure.title('Успешная регистрация нового пользователя')
    def test_register_unique_user(self, create_user):
        assert create_user[0] == 200 and create_user[1]['success'] == True

    @allure.title('Регистрация пользователя с неуникальными данными')
    def test_register_not_unique_user(self, create_user):
        not_unique_user = RegisterMethods().user_registration(data.EMAIL, data.PASSWORD, data.NAME, False)
        assert not_unique_user[0] == 403 and not_unique_user[1]['success'] == False

    @pytest.mark.parametrize(
        'email, password, name, need_generate_data',
        [
            [data.EMAIL, '', data.NAME, False],
            ['', data.PASSWORD, data.NAME, False],
            [data.EMAIL, data.PASSWORD, '', False]
        ]
    )
    @allure.title('Регистрация пользователя без заполнения необходимых полей')
    def test_register_with_not_filled_fields(self, email, password, name, need_generate_data):
        user_with_not_filled_fields = RegisterMethods.user_registration(email, password, name, need_generate_data)
        assert user_with_not_filled_fields[0] == 403 and user_with_not_filled_fields[1] == data.ERROR_REQUIRED_FIELDS