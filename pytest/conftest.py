from pytest import fixture
from selenium import webdriver

# @fixture(scope='function')
# def chrome_browser():
#     return webdriver.Chrome()


@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser

    """Teardown"""
    print('Tearing down chrome browser')
