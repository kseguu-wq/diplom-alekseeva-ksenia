# Ксения Алексеева, 41-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

# проверяем, что заказ создаётся
def test_create_order():
    response = requests.post(configuration.get_url(configuration.CREATE_ORDER_PATH), json=data.order_body)
    assert response.status_code == 201

# проверяем, что созданный заказ можно найти по треку
def test_get_order_by_track():
    # создаём заказ и получаем его трек
    create_response = requests.post(configuration.get_url(configuration.CREATE_ORDER_PATH), json=data.order_body)
    track = create_response.json()["track"]
    
    # находим заказ по этому треку
    get_response = requests.get(configuration.get_url(configuration.GET_ORDER_PATH), params={"t": track})
    assert get_response.status_code == 200