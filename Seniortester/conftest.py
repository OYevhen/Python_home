import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.headless = False
    # options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()

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