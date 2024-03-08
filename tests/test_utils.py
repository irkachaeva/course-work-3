from src.utils import get_info


def test_get_info():
    assert type(get_info('../src/operations.json')) == list

