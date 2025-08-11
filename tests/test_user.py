import pytest

from helpers import generate_random_string
from methods.user_methods import UserMethods


class TestUser:

    @pytest.mark.parametrize(
        'edit_field, new_data',
        [
            ["name", generate_random_string(10)],
            ["email", generate_random_string(10)],
        ]
    )
    def test_edit_user_success(self, create_user, edit_field, new_data):
        json = {edit_field: new_data}
        UserMethods.edit_user(create_user[1]['accessToken'], json)
        get_data_user = UserMethods.get_user(create_user[1]['accessToken'])
        assert get_data_user[1]['user'][edit_field] == new_data


    def test_edit_user_without_authorization(self, create_user):
        pass
        # assert user_without_authorization[0] == 403 and user_without_authorization[1]['success'] == False
