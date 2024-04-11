import pytest
import requests

from utils import register_new_courier_and_return_login_password


@pytest.fixture
def new_courier():
    return register_new_courier_and_return_login_password()


@pytest.fixture
def new_courier_id():
    login, password, first_name = register_new_courier_and_return_login_password()

    payload = {
        "login": login,
        "password": password
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    return response.json()['id']