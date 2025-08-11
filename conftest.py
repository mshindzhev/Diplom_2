import pytest

import data
from methods.user_methods import UserMethods
from methods.register_methods import RegisterMethods


@pytest.fixture
def create_user():
    create_user = RegisterMethods().user_registration(data.EMAIL, data.PASSWORD, data.NAME, False)
    yield create_user
    UserMethods.delete_user(create_user[1]['accessToken'])