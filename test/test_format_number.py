import pytest
from numberformatter import NumberFormatter

@pytest.fixture
def formatter():
    return NumberFormatter('numbers_dictionary.csv')

def test_format_number_1_digit(formatter):
    number_1_digit = ('uno','1')
    formatted_number = formatter.format_number(number_1_digit[0])
    assert formatted_number is not None
    assert formatted_number == number_1_digit[1]

def test_format_numbers_1_digit(formatter):
    numbers_1_digit = ('cero','uno','una','un','cinco','nueve')
    numbers_1_digit_target = ('0','1','1','1','5','9')
    formatted_numbers = formatter.format_numbers(numbers_1_digit)
    for i, formatted_number in enumerate(formatted_numbers):
        assert formatted_number is not None
        assert formatted_number == numbers_1_digit_target[i]

def test_format_number_2_digits(formatter):
    number_2_digits = ('treinta','30')
    formatted_number = formatter.format_number(number_2_digits[0])
    assert formatted_number is not None
    assert formatted_number == number_2_digits[1]

def test_format_numbers_2_digits(formatter):
    numbers_1_digit = ('diez','once','veinte','veintiuno','veinticinco','treinta y uno','cuarenta y una','noventa y nueve')
    numbers_1_digit_target = ('10','11','20','21','25','31','41','99')
    formatted_numbers = formatter.format_numbers(numbers_1_digit)
    for i, formatted_number in enumerate(formatted_numbers):
        assert formatted_number is not None
        assert formatted_number == numbers_1_digit_target[i]

def test_format_numbers_3_digits(formatter):
    numbers_1_digit = ('cien','ciento un','ciento uno','ciento una','ciento dieciocho','doscientos diez','trescientos cincuenta y ocho',
    'quinientos treinta y una')
    numbers_1_digit_target = ('100','101','101','101','118','210','358','531')
    formatted_numbers = formatter.format_numbers(numbers_1_digit)
    for i, formatted_number in enumerate(formatted_numbers):
        assert formatted_number is not None
        assert formatted_number == numbers_1_digit_target[i]

def test_format_numbers_4_digits(formatter):
    numbers_1_digit = ('mil','mil y uno','dos mil','mil cincuenta y siete','mil cuatrocientos sesenta y dos','mil novecientos ochenta','tres mil treinta',
    'cinco mil setecientos cuarenta','seis mil doscientos treinta y cuatro')
    numbers_1_digit_target = ('1000','1001','2000','1057','1462','1980','3030','5740','6234')
    formatted_numbers = formatter.format_numbers(numbers_1_digit)
    for i, formatted_number in enumerate(formatted_numbers):
        assert formatted_number is not None
        assert formatted_number == numbers_1_digit_target[i]

def test_format_numbers_5_digits(formatter):
    numbers_1_digit = ('diez mil','diez mil y uno','diez mil ochenta y uno','veinte mil cuatrocientos sesenta y dos',
    'treinta y cuatro mil doscientos noventa y nueve','cincuenta y dos mil','cincuenta y tres mil y dos','cincuenta y cuatro mil treinta y cuatro')
    numbers_1_digit_target = ('10000','10001','10081','20462','34299','52000','53002','54034')
    formatted_numbers = formatter.format_numbers(numbers_1_digit)
    for i, formatted_number in enumerate(formatted_numbers):
        assert formatted_number is not None
        assert formatted_number == numbers_1_digit_target[i]

def test_format_numbers_6_digits(formatter):
    numbers_1_digit = ('doscientos mil','trescientos mil y uno','cuatrocientos mil ochenta y uno','cuatrocientos treinta y tres mil doscientos',
    'quinientos treinta y un mil cuatrocientos sesenta y cinco')
    numbers_1_digit_target = ('200000','300001','400081','433200','531465')
    formatted_numbers = formatter.format_numbers(numbers_1_digit)
    for i, formatted_number in enumerate(formatted_numbers):
        assert formatted_number is not None
        assert formatted_number == numbers_1_digit_target[i]