from pytest import mark


@mark.smoke
@mark.engine
def test_engine_functions_as_expected():
    assert True

# pytest - m "smoke and engine"
# pytest - m "smoke or engine"
# pytest - m "not engine"


"""
Aby tworzyć raporty z testów można zainstalować pytest-html
następnie w terminalu można przygotować raport używając polecenia 
pytest --html="report.html"
"""