#Макаренко Артем Игоревич, 10-поток, инжерен QA плюс, диплом.
import Created_Order

def test_search_order_status_code_200():
    assert Create_Order.search_order().status_code == 200
