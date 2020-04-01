import pytest
from copy import copy
from pytest_bdd import scenario, given, when, then
from requests import get, put, post, delete
from src.utils.request_sender import send_request, reset_service_data


def setup():
    reset_service_data()


@scenario('../../features/test_negative.feature', 'check getting character by wrong filter')
def test_get_by_wrong_filter(context):
    pass


@when('send request about getting character by filter with incorrect filter')
def send_wrong_field_request(context):
    context.sending_data = {'wrong_field': 'wrong value'}
    context.service_response = send_request(get, request_data=context.sending_data)


@then('validate response error about wrong field')
def validate_wrong_field_response(context):
    response_error = context.service_response.json().get('error')
    assert response_error == "name parameter is required"


@scenario('../../features/test_negative.feature', 'check updating not existing character')
def test_update_non_exist_character(context):
    pass


@when('send request about updating character')
def send_not_existing_character_update(context):
    context.sending_data = {'name': 'some wrong name'}
    context.service_response = send_request(put, request_data=context.sending_data)


@then('validate not existing error in response')
def validate_not_existing_update_response(context):
    response_error = context.service_response.json().get('error')
    assert response_error == "No such name"


@scenario('../../features/test_negative.feature', 'check adding character with full db')
def test_add_character_full_db(context):
    pass


@given('add five hundred characters')
def add_full_db(new_character):
    sending_data = copy(new_character)
    for character_seq in range(500):
        sending_data['name'] = f"{new_character['name']}_{character_seq}"
        send_request(post, request_data=sending_data)


@when('send request about adding character')
def send_adding_request(context, new_character):
    context.service_response = send_request(post, request_data=new_character)


@then('validate db error in response')
def validate_db_error(context):
    response_error = context.service_response.json().get('error')
    assert response_error == "Collection can't contain more than 500 items"


@scenario('../../features/test_negative.feature', 'check adding character with not all fields')
def test_add_character_not_all_fields(context):
    pass


@when('send request about adding character with partial data')
def send_add_partial_data(context, new_character):
    sending_data = copy(new_character)
    sending_data.pop("name")
    context.service_response = send_request(post, request_data=sending_data)


@then('validate error about partial data in response')
def validate_partial_data_error(context):
    response_error = context.service_response.json().get('error')
    assert response_error == "name: ['Missing data for required field.']"


@scenario('../../features/test_negative.feature', 'check deleting not existing character')
def test_delete_non_exist_character(context):
    pass


@when('send request about deleting not existing character')
def delete_wrong_character(context):
    context.sending_data = {'name': 'some wrong name'}
    context.service_response = send_request(delete, request_data=context.sending_data)


@then('validate not existing error in response for deleting')
def validate_not_existing_update_response(context):
    response_error = context.service_response.json().get('error')
    assert response_error == "No such name"


@pytest.mark.parametrize("sending_value", [
    "%:!",
    "",
    0
])
def test_wrong_data_type(sending_value):
    sending_data = {'name': sending_value}
    service_response = send_request(put, request_data=sending_data)
    response_error = service_response.json().get('error')
    error_type = {
        "%:!": 'No such name',
        "": "name: ['Length must be between 1 and 350.']",
        0: "name: ['Not a valid string.']"
    }.get(sending_value)
    assert error_type == response_error


def teardown():
    reset_service_data()
