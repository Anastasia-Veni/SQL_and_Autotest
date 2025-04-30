import configuration
import requests

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body)

def get_order_by_track(track):
    params = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH, params=params)
