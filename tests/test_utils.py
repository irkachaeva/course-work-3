import pytest

from src.utils import get_info
from src.utils import get_info_filter
from src.utils import get_sorted_list
from src.utils import format_operation

def test_get_info():
    assert type(get_info('../tests/test_data.json')) == list
    assert len(get_info('../tests/test_data.json')) > 0


def test_get_info_filter():
    assert len(get_info_filter(get_info('../tests/test_data.json'), "EXECUTED")) > 0
    assert get_info_filter(get_info('../tests/test_data.json'), "EXECUTED")[0]["state"] == "EXECUTED"
    assert get_info_filter(get_info('../tests/test_data.json'), "EXECUTED")[-1]["state"] == "EXECUTED"
    assert type(get_info_filter(get_info('../tests/test_data.json'), "EXECUTED")) == list

def test_get_sorted_list():
    data_for_test = get_info_filter(get_info('../tests/test_data.json'), "EXECUTED")
    assert get_sorted_list(data_for_test,2)[0]["date"] == '2019-08-26T10:50:58.294041'
    assert len(get_sorted_list(data_for_test, 2)) == 2






