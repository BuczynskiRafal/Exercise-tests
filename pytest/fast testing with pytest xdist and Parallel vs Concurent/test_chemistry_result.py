"""
pip install pytest-xdist
to narzędzie pozwala dużo szybciej wykonać testy.
Poniższe testy za pomoaca time slep wykonują się 5 sekun
w całości wykonują się 20 sekund
pytest -s -v
-s wyrzuci w konsoli printy z testów
-v da więcej informacji o testach
używając xdist można wykonać je znacznie szybciej

xdist wykonuje wielowątkowo procesy(testy)
pytest -s -v -n2

-n2 oznacza że uruchomią się 2 testy na raz
w efekcie poniższe testy wykonywały się 10sekund

pytest -s -v -n4
-n4 oznacza że uruchomią się 2 testy na raz
w efekcie poniższe testy wykonywały się 5 sekund

"""

import time


def test_result_1_completes_as_expected():
    time.sleep(5)
    print("Result 1 has completed.")


def test_result_2_completes_as_expected():
    time.sleep(5)
    print("Result 2 has completed.")


def test_result_3_completes_as_expected():
    time.sleep(5)
    print("Result 3 has completed.")


def test_result_4_completes_as_expected():
    time.sleep(5)
    print("Result 4 has completed.")


