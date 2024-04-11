import requests
import allure


class TestOrderList:

    @allure.title('Проверка кода API на list всех заказов')
    def test_success_order_list_code(self, new_courier_id):

        params = {'courierId': new_courier_id}

        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/', params=params)
        assert response.status_code == 200

    @allure.title('Проверка тела ответа API на list всех заказов')
    def test_success_order_list_body(self, new_courier_id):

        params = {'courierId': new_courier_id}

        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/', params=params)
        assert 'orders' in response.json()
