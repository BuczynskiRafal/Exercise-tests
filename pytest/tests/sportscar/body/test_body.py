import time

import pytest
from pytest import mark


# @mark.ui
# def test_body_website(self, chrome_browser):
#     first_page = chrome_browser
#     first_page.get('https://docs.pytest.org/en/latest/explanation/fixtures.html')
#
#     # time.sleep(5)
#     #
#     # second_page = chrome_browser
#     # second_page.get(
#     #     'https://www.google.com/search?q=second+page&oq=second+page&aqs=chrome..69i57j46i19j0i19l8.6134j0j7&sourceid=chrome&ie=UTF-8')
#
#     assert True


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
