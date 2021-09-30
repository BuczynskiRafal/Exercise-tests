import random
from unittest.mock import patch


def get_code():
    rand_int = random.randint(1-9)
    return f'XC-{rand_int}'


with patch('random.randint') as mock_randint:
    mock_randint.return_value = 5
    print(get_code())


with patch('random.randint') as mock_randint:
    mock_randint.return_value = 2
    print(get_code())


@patch('random.randint')
def test_get_code_3(mock_randint):
    mock_randint.return_value = 3
    code = get_code()
    assert code == 'XC-3'

test_get_code_3()