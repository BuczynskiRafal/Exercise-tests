import pytest
from pytest import mark


@mark.body
class TestsBody:
    @mark.smoke
    def test_body_functions_as_expected(self):
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True

if __name__ == '__main__':
    pytest.main()
