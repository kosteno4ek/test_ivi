from pytest_bdd import scenario, given, when, then
from requests import get, put, post, delete
from src.utils.request_sender import send_request, reset_service_data
from src.utils.test_data import character_data


def setup():
    reset_service_data()


@scenario('../../features/test_smoke.feature', 'check adding character')
def test_add_character(context):
    pass


@when('send request about adding character')
def send_add_request(context):
    context.service_response = send_request(post, request_data=character_data)


@then('validate this character in response')
def validate_add_character_response(context):
    assert context.service_response.status_code == 200
    response_data = context.service_response.json().get('result')
    assert character_data == response_data


@scenario('../../features/test_smoke.feature', 'check getting all characters')
def test_get_all_characters(context):
    pass


@given('send request to add new character')
def add_character_request():
    send_request(post, request_data=character_data)


@when('send request about getting all characters')
def send_get_all_characters_request(context):
    context.service_response = send_request(get)


@then('validate our character in response')
def validate_all_characters_response(context):
    response_data = context.service_response.json().get('result')
    assert context.service_response.status_code == 200
    assert len(response_data) > 1
    assert character_data in response_data


@scenario('../../features/test_smoke.feature', 'check getting character by filter')
def test_get_character_by_name(context):
    pass


@given('send request to add new character for filtering request')
def send_add_msg():
    send_request(post, request_data=character_data)


@when('send request about getting character by filter')
def send_filter_request(context):
    sending_data = {'name': character_data.get('name')}
    context.service_response = send_request(get, request_data=sending_data)


@then('validate character in response')
def validate_updating_response(context):
    response_data = context.service_response.json().get('result')
    assert context.service_response.status_code == 200
    assert response_data == character_data


@scenario('../../features/test_smoke.feature', 'check updating character')
def test_update_character(context):
    pass


@given('send request to add new character for its updating')
def send_new_character():
    send_request(post, request_data=character_data)


@when('send request about updating character')
def send_update_request(context):
    context.sending_data = character_data
    context.sending_data['universe'] = 'test universe'
    context.service_response = send_request(put, request_data=context.sending_data)


@then('validate character with new value in fields in response')
def validate_update_response(context):
    response_data = context.service_response.json().get('result')
    assert context.service_response.status_code == 200
    assert context.sending_data == response_data


@scenario('../../features/test_smoke.feature', 'check deleting character')
def test_delete_character(context):
    pass


@given('send request to add new character for its deleting')
def send_adding_request():
    send_request(post, request_data=character_data)


@when('send request about deleting character')
def send_delete_request(context):
    context.sending_data = {'name': character_data.get('name')}
    context.service_response = send_request(delete, request_data=context.sending_data)


@then('validate character in response when delete')
def validate_deleting_response(context):
    response_data = context.service_response.json().get('result')
    assert context.service_response.status_code == 200
    assert response_data == "Hero {} is deleted".format(context.sending_data.get('name'))


def teardown():
    reset_service_data()
