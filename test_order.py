#Макаренко Артем Игоревич, 10-поток, инжерен QA плюс, диплом.
import Created_Order

def test_search_order_status_code_200():
    status_code = Created_Order.search_order().status_code
    assert status_code == 200
    if status_code == 200:
        print("Тест пройден, код 200")
    else:
        print("Потрачено")
