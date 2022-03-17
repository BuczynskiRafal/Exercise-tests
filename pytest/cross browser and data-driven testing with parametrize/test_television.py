"""
parametryzacja testów
używając markera 'parametrize' zbudowałem listę nazw
producentów telewizorów przez co test powinien się w
ykonać na każdym elemencie listy
"""


from pytest import mark

@mark.skip
@mark.parametrize('tv_brand', [
    ('Samsung', ),
    ('Sony', ),
    ('Panasonic',),
])
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected.")


def test_browser_can_navigate_to_training_ground(browser):
    browser.get('https://www.google.pl/')


import json
from pytest import fixture
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / 'test_data.json'

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params=load_test_data(DATA_PATH))
def test_data(request):
    data = request.param
    return data