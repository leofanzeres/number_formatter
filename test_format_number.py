import pytest
from numberformatter import NumberFormatter

@pytest.fixture
def formatter():
    return NumberFormatter('numbers_dictionary.csv')

@pytest.fixture
def number():
    return 'uno'

@pytest.fixture
def numbers_dict_csv(formatter):
    return 'numbers_dictionary.csv'

def test_format_number_1_digit(formatter, number):
    assert formatter.format_number(number) == formatter.load_dictionary().get(number)


