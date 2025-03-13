# Мария Черепахина, Selfpaсed, 11_финальный спринт. Инженер по тестированию плюс

import sender_stand_request
import data


def test_get_order():
    response_order = sender_stand_request.create_order(data.craete_body)
    kod_track = response_order.json()["track"]
    response_get_order = sender_stand_request.get_track(kod_track)
    assert response_get_order.status_code == 200
