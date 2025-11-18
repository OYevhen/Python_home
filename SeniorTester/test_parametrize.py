#https://www.youtube.com/watch?v=pqIoyCJMBvM&list=PLRVGb5te8vVH3DJKxtRQp3-68_gQ3CEqx&index=7

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


#@pytest.mark.parametrize('creds', ['324343545', '565434322', '123131415'])      #or ('creds', [(****, ****), (****, ****)])

# @pytest.mark.parametrize(
#     'creds',
#     [
#         pytest.param('324343545', id ='324343545')
#         pytest.param('565434322', id ='565434322')
#         pytest.param('123131415', id ='123131415')
#
#     ]
# )

@pytest.mark.skip
def test_login(creds):
    tel = creds
    driver = webdriver.Firefox()
    driver.get("https://new.novaposhta.ua/auth/login-private-person")
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, 'input[type="tel"]').send_keys(tel)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    check = driver.find_element(By.CLASS_NAME, 'start__title').text
    assert check == 'Створити профіль'

@pytest.fixture()
def page(request):
    driver = webdriver.Firefox()
    param = request.param
    if param == 'test_news':
        driver.get("https://novaposhta.ua/news/")
    elif param == 'dostavka_bonusiv':
        driver.get("https://novaposhta.ua/dostavka-bonusiv")
    return driver

@pytest.mark.parametrize('page', ['test_news'], indirect=True)
def test_news(page):
    title = page.find_element(By.CSS_SELECTOR, 'div[plerdy-tracking-id="53973043901"]')
    assert title.text == 'Новини'

@pytest.mark.parametrize('page', ['dostavka_bonusiv'], indirect=True)
def test_dostavka_bonusiv(page):
    title = page.find_element(By.XPATH, "//div[contains(@class, 'md:text-6xl')]")
    assert title.text == 'Доставка бонусів'