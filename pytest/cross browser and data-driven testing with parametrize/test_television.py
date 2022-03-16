"""
parametryzacja testów
używając markera 'parametrize' zbudowałem listę nazw
producentów telewizorów przez co test powinien się w
ykonać na każdym elemencie listy
"""


from pytest import mark


@mark.parametrize('tv_brand', [
    ('Samsung', ),
    ('Sony', ),
    ('Panasonic',),
])
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected.")

