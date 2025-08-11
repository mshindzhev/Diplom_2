import pytest

import data
from methods.login_methods import LoginMethods


class TestLogin:

    def test_login_success(self, create_user):
        user_login = LoginMethods.user_login(data.EMAIL, data.PASSWORD)
        assert user_login[0] == 200 and user_login[1]['success'] == True

    @pytest.mark.parametrize('email, password',
                             [
                                 [data.EMAIL, data.INVALID_PASSWORD],
                                 [data.INVALID_EMAIL, data.PASSWORD],
                                 [data.INVALID_EMAIL, data.INVALID_PASSWORD]
                             ])
    def test_login_with_invalid_data(self, create_user, email, password):
        user_login = LoginMethods.user_login(email, password)
        assert user_login[0] == 401 and user_login[1]['success'] == False

