import pytest

import data
from methods.delete_methods import DeleteMethods
from methods.register_methods import RegisterMethods


# @pytest.fixture
# def register_user():
#     register_user = RegisterMethods()
#     yield register_user.user_registration(email=data.EMAIL, password=data.PASSWORD, name=data.NAME)
#     DeleteMethods.delete_user()