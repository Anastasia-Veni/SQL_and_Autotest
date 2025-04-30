import data
import sender_stand_request

def test_create_and_get_order():
    # Создать заказ
    response = sender_stand_request.post_new_order(data.order_body)
    assert response.status_code == 201
    track = response.json()["track"]

    # Получить заказ по треку
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200
    assert get_response.json()["order"]["track"] == track
