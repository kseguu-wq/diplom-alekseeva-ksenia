import requests
import configuration
import data

def test_create_and_get_order():
    # Создание заказа
    response_create = requests.post(configuration.get_url(configuration.CREATE_ORDER_PATH), json=data.order_body)
    assert response_create.status_code == 201

    # Получение трека
    track = response_create.json()["track"]

    # Получение заказа по треку
    response_get = requests.get(configuration.get_url(configuration.GET_ORDER_PATH), params={"t": track})
    assert response_get.status_code == 200