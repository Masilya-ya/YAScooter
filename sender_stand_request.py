import config
import requests


def create_order(body): # функция создания заказа
    response_order = requests.post(config.URL_SERVICE + config.CREATE_ZAKAZ, json=body)
    return response_order


def get_track(number_track): # функция получения заказа по номеру трека
    response_get = requests.get(config.URL_SERVICE + config.GET_ZAKAZ + str(number_track))
    return response_get