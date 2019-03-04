import pytest


@pytest.fixture(scope='module')
def a_string():
    print("\nBefore yield")
    return   'Hi, how are you?'
    print("\nAfter yield")


@pytest.fixture(scope='module')
def an_empty_list():
    return []


@pytest.fixture(scope='module')
def a_list_with_data():
    return [1, 2, 3, 4, 5]


def test_empty_list(an_empty_list):
    assert len(an_empty_list) == 0


def test_list_is_not_empty(a_list_with_data):
    assert len(a_list_with_data) != 0


def test_max_number_in_list(a_list_with_data):
    assert max(a_list_with_data) > 4


def test_strings_contains_string(a_string):
    assert "how" in a_string


def test_strings_contains_string_another_way(a_string):
    assert a_string.find("how") != -1

