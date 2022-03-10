from pytest import mark


@mark.smoke
@mark.engine
def test_engine_functions_as_expected():
    assert True

# pytest - m "smoke and engine"
# pytest - m "smoke or engine"
# pytest - m "not engine"