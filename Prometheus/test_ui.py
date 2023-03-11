import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_incorrect_username():
    #Створення обєкту для курування браузером
    driver = webdriver.Chrome(
        service=Service(r'C:/Users/orely/PycharmProjects/Python_home/Prometheus' + 'chromedriver.exe')
    )
    # відкриваємо сторінку браузером
    driver.get("https://github.com/login")

    # Знаходимо поле в яке будемо вводити неправильне імя користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильне імя користувача або поштову адресу
    login_elem.send_keys("test")


    # Знаходимо поле в яке буде введено невірний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    # Знаходимо кнопку sign in
    btn_element = driver.find_element(By.NAME, "commit")

    # клік
    btn_element.click()

    # Превірка назви сторінки
    assert driver.title == "Sign in to GitHub · GitHub"
    # time.sleep(3)

    # закриваємо браузер
    driver.close()