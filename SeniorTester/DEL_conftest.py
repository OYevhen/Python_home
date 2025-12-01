import sys
from pathlib import Path

from _pytest.fixtures import SubRequest

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# def pytest_addoption(parser):
#    parser.addoption('--browser')

@pytest.fixture
def driver(request: SubRequest):
    options = Options()
    options.headless = False
    # options.add_argument('--headless')
    if request.config.getoption('--browser').upper() == 'FF':
        driver = webdriver.Firefox(options=options)
    elif request.config.getoption('--browser').lower() == 'chrome':
        driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")   #по замовчуванню
def  separator():
    print('starting')
    yield
    print('done')

@pytest.fixture(scope="session")
def all_tests():
    print('\nstarting tests')
    yield
    print('all tests done')

@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    return driver