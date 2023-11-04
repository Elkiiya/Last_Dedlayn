import Config
import Data
import requests

def post_new_order(body):
    return requests.post(Config.URL_SERVICE + Config.CREATE_ORDER_PATH,
                         json=body)

def get_track():
    track_body = post_new_order(Data.User_body)
    track_put = str(track_body.json()['track'])
    return track_put

def search_order(track_number):
    return requests.get(Config.URL_SERVICE + Config.SEARCH_ORDER_PATH + "?t=" + track_number)
