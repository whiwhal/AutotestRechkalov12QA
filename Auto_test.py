import configuration
import data
import sender_stand_request

# Автотест
def test_order_creation():

# 1. Выполнить запрос на создание заказа.
    response = sender_stand_request.create_order(data.order_body)

# 2. Сохранить номер трека заказа.
    track_number = response.json()["track"]

# 3. Выполнить запрос на получения заказа по треку заказа.
    response_order = sender_stand_request.get_order(track_number)

# 4. Проверить, что код ответа равен 200.
    assert response_order.status_code == 200
    data_order = response_order.json()
