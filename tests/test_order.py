import pytest
import requests
import allure
from static import color_order_data
from utils import build_dictionary


class TestLogin:

    # todo параметризацию добавить
    @pytest.mark.parametrize('color',
                             color_order_data)
    @allure.title('Проверка разных выборов цвета')
    def test_success_create_order_color(self, color):
        payload = build_dictionary()
        payload['color'] = color
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        assert response.status_code == 201
        # {'code': 500, 'message': 'values.map is not a function'}

    @allure.title('Проверка ответа API на получение id после логинизации')
    def test_success_create_order_track_in_body(self):
        payload = build_dictionary()
        payload['color'] = []
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        assert response.json().get('track')
