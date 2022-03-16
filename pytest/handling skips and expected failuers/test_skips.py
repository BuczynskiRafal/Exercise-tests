from pytest import mark

"""
Jeśli chcesz pominąć test można zaimportować marker 'skip'.
oznaczając @mark.skip test zostanie pominięty.
wywołanie 'pytest dir\doc.py -v'
można dodac komentaż dlaczego tes jest pomijany @mark.skip(reason='broken by deploy somenumber')
można dodać flagę -rs wywołanie 'pytest dir\doc.py -v -rs pokaże w oddzielnych wierszach dlaczego testy są pomijane
"""

"""
xfail oznacza, że z jakiegoś powodu spodziewasz 
się niepowodzenia testu . Typowym przykładem jest 
test funkcji jeszcze nie zaimplementowanej lub błąd, 
który nie został jeszcze naprawiony. Jeśli test 
przejdzie pomyślnie, mimo że oczekuje się niepowodzenia 
(oznaczony symbolem pytest.mark.xfail), jest to test 
xpass i zostanie zgłoszony w podsumowaniu testu.
wywołanie 'pytest dir\doc.py -v'
"""


@mark.skip(reason='broken by deploy somenumber')
def test_first_pass():
    assert True


@mark.skip
def test_second_failure():
    assert False


def test_third_pass():
    assert True


@mark.skip
def test_fourth_failure():
    assert False


@mark.wip
def test_this_test_needs_work():
    assert True


@mark.xfail(reason='fifth test should be failure')
def test_fifth_failure():
    assert False
