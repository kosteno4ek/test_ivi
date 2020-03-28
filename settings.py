import logging
import sys
from os import environ

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

TEST_URI = "http://rest.test.ivi.ru/v2"

TEST_LOGIN = environ.get("LOGIN")
TEST_PASSWORD = environ.get("PASSWORD")

EDIT_URI = "/character"
GET_UTI = "/characters"
RESET_URI = "/reset"
