from requests.auth import HTTPBasicAuth
from requests import get, put, post, delete
from settings import TEST_URI, TEST_LOGIN, TEST_PASSWORD, RESET_URI, GET_UTI, EDIT_URI


def send_request(method, request_data=None):
    sending_args = {
        get: {"params": request_data},
        post: {"json": request_data},
        put: {"json": request_data},
        delete: {"params": request_data}
    }.get(method)
    sending_args["url"] = f"{TEST_URI}{GET_UTI if not request_data else EDIT_URI}"
    sending_args['auth'] = HTTPBasicAuth(TEST_LOGIN, TEST_PASSWORD)
    print(f'sending params > {sending_args}')
    response = method(**sending_args)
    print(f'incoming response < {sending_args}')
    return response


def reset_service_data():
    post(f"{TEST_URI}{RESET_URI}", auth=HTTPBasicAuth(TEST_LOGIN, TEST_PASSWORD))
