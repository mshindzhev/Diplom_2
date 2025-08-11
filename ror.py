from conftest import create_user
from methods.user_methods import UserMethods
from methods.login_methods import LoginMethods
from methods.register_methods import RegisterMethods

register_user = RegisterMethods.user_registration(password='qwerty123')
print(register_user)
# print(LoginMethods.user_login())
# print(DeleteMethods.delete_user('Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY4OTczODU0OWVkMjgwMDAxYjY3NDc5NyIsImlhdCI6MTc1NDc0MDgyMCwiZXhwIjoxNzU0NzQyMDIwfQ.ETUupu6Y0ty2buRFbVBvcHkRzjBMVmpcsqSQd3nfurE'))
# register_user[1]['accessToken'])
name = register_user.json()['name']
UserMethods.edit_user(name)