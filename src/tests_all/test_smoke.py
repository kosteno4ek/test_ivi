from requests import get, put, post, delete
from src.utils.request_sender import send_request, reset_service_data


def setup():
    reset_service_data()


def test_add_character(new_character):
    service_response = send_request(post, request_data=new_character)
    assert service_response.status_code == 200
    response_data = service_response.json().get('result')
    assert new_character == response_data


def test_get_all_characters(new_character):
    send_request(post, request_data=new_character)
    service_response = send_request(get)

    response_data = service_response.json().get('result')
    assert service_response.status_code == 200
    assert len(response_data) > 1
    assert new_character in response_data


def test_get_character_by_name(new_character):
    send_request(post, request_data=new_character)
    sending_data = {'name': new_character.get('name')}
    service_response = send_request(get, request_data=sending_data)

    response_data = service_response.json().get('result')
    assert service_response.status_code == 200
    assert response_data == new_character


def test_update_character(new_character):
    send_request(post, request_data=new_character)

    sending_data = new_character
    sending_data['universe'] = 'test universe'
    service_response = send_request(put, request_data=sending_data)

    response_data = service_response.json().get('result')
    assert service_response.status_code == 200
    assert sending_data == response_data


def test_delete_character(new_character):
    send_request(post, request_data=new_character)

    sending_data = {'name': new_character.get('name')}
    service_response = send_request(delete, request_data=sending_data)

    response_data = service_response.json().get('result')
    assert service_response.status_code == 200
    assert response_data == "Hero {} is deleted".format(sending_data.get('name'))


def teardown():
    reset_service_data()
