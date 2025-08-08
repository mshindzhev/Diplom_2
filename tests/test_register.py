import pytest

import data
from methods.register_methods import RegisterMethods


class TestRegister:

    def test_register_unique_user(self):
        register_user = RegisterMethods().user_registration()
        assert register_user[0] == 200 and register_user[1]['success'] == True

    @pytest.mark.parametrize(
        'email, password, name, need_generate_data',
        [
            [data.EMAIL, '', data.NAME, False],
            ['', data.PASSWORD, data.NAME, False],
            [data.EMAIL, data.PASSWORD, '', False]
        ]
    )
    def test_register_with_not_filled_fields(self, email, password, name, need_generate_data):
        data_register = RegisterMethods.user_registration(email, password, name, need_generate_data)
        assert data_register.status_code == 403 and data_register.text == data.ERROR_REQUIRED_FIELDS