from pytest import fixture
from selenium import webdriver
from config import Config

# @fixture(scope='function')
# def chrome_browser():
#     return webdriver.Chrome()


@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser

    """Teardown"""
    print('Tearing down chrome browser')


"""
Pass different values to a test function, depending on command line options
Przekaż różne wartości do funkcji testowej, w zależności od opcji wiersza poleceń
Załóżmy, że chcemy napisać test, który zależy od opcji wiersza poleceń. Oto podstawowy wzór, aby to osiągnąć:
"""
# content of test_sample.py
def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0  # to see what was printed

"""
For this to work we need to add a command line option and provide the cmdopt through a fixture function:
Aby to zadziałało, musimy dodać opcję wiersza poleceń i udostępnić cmdopt funkcję Through :
"""
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests against."
    )

@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


"""
Środowisko można ustawić w terminalu używając polecenia 
pytest --env qa
pytest --env dev
"""


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg
