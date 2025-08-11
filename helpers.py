import random
import string

import allure


@allure.step('Генерируем данные для регистрации пользователя')
def generate_data_for_registration():
    email = f'{generate_random_string(10)}@mail.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)
    return {
    "email": email,
    "password": password,
    "name": name
}

@allure.step('Генерируем строку для данных пользователя')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string