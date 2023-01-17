import pytest
from format_number import format_number

number_format_dict = {'mil veintiuno':1021}

@pytest.fixture
def number_text():
    return 'mil veintiuno'

#def test_split_text():
    

def test_format_number(number_text):
    assert format_number(number_text) == number_format_dict.get(number_text)

