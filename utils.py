import requests
import random
import string

from faker import Faker


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def register_new_courier_and_return_login_password():

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


def build_dictionary():
    faker = Faker()
    payload = {
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "address": faker.text(),
        "metroStation": random.choice(range(1, 15)),
        "phone": faker.phone_number(),
        "rentTime": random.choice(range(1, 10)),
        "deliveryDate": faker.date(),
        "comment": faker.text(),
        "color": [
            "BLACK"
        ]
    }
    return payload

