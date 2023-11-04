#Макаренко Артем Игоревич, 10-поток, инжерен QA плюс, диплом.
import Created_Order

def test_search_order_status_code_200():
    track_number = Created_Order.get_track()
    assert Created_Order.search_order(track_number).status_code == 200
