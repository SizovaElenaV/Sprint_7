import requests
import allure
from utils import register_new_courier_and_return_login_password, generate_random_string


class TestCreateCourier:

    @allure.title('Проверка кода API создания курьера')
    def test_create_code(self):
        login, password, first_name = generate_random_string(10), generate_random_string(10), generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 201

    @allure.title('Проверка тела API создания курьера')
    def test_create_body(self):
        login, password, first_name = generate_random_string(10), generate_random_string(10), generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.json()['ok']

    @allure.title('Проверка кода API на создания дублирующегося курьера')
    def test_create_duplicate_code(self):
        login, password, first_name = register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 409

    @allure.title('Проверка тела API создания дублирующегося курьера')
    def test_create_duplicate_body(self):
        login, password, first_name = register_new_courier_and_return_login_password()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Проверка кода API на обязательные поля при создании курьера')
    def test_create_required_fields_code(self):
        login = generate_random_string(10)

        payload = {
            "login": login
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 400

    @allure.title('Проверка тела API на обязательные поля при создании курьера')
    def test_create_required_fields_body(self):
        login = generate_random_string(10)

        payload = {
            "login": login
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'
