import pytest
from numberformatter import NumberFormatter

@pytest.fixture
def formatter():
    return NumberFormatter('numbers_dictionary.csv')

@pytest.fixture
def number_1_digit():
    return 'uno'

@pytest.fixture
def numbers_1_digit():
    return 'test/numbers_list_1_digit.txt'

@pytest.fixture
def number_2_digits():
    return 'diez'

@pytest.fixture
def numbers_dict_csv(formatter):
    return 'numbers_dictionary.csv'

def test_format_number_1_digit(formatter, number_1_digit):
    assert formatter.format_number(number_1_digit) == formatter.load_dictionary().get(number_1_digit)

def test_format_numbers_1_digit(formatter, numbers_1_digit):
    formatted_numbers = formatter.format_numbers(numbers_1_digit)
    with open(numbers_1_digit) as f:
        lines = f.readlines()
    dict = formatter.load_dictionary()
    for i, number in enumerate(formatted_numbers):
        assert number == dict.get(lines[i])


