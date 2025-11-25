import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    return chrome_driver

def test_cost(driver):
    driver.get("https://novaposhta.ua/")
    send = driver.find_element(By.CSS_SELECTOR, 'div[plerdy-tracking-id="97380723901"]')
    tarifs = driver.find_element(By.CSS_SELECTOR, 'a[plerdy-tracking-id="65298410601"]')
    # ActionChains(driver).move_to_element(send).pause(1).move_to_element(tarifs).perform()
    actions = ActionChains(driver)
    actions.move_to_element(send)
    actions.pause(1)
    actions.move_to_element(tarifs)
    actions.perform()

def test_new_tab_promo(driver):
    driver.get("https://novaposhta.ua/")
    promo = driver.find_element(By.CSS_SELECTOR, 'a[href="/promotions"]')
    ActionChains(driver).key_down(Keys.CONTROL).click(promo).key_up(Keys.CONTROL).perform()
    time.sleep(2)


