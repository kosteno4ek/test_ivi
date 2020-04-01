import pytest


@pytest.fixture
def context():
    class Context:
        pass

    return Context()


@pytest.fixture
def new_character():
    character_data = {
        "name": "test character",
        "universe": "Marvel Universe",
        "education": "High School (unfinished)",
        "weight": 104,
        "height": 1.90,
        "identity": "Publicly known"
    }
    return character_data
