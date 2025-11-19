
from selenium.webdriver.common.by import By

def test_button2_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    assert browser.find_element(By.LINK_TEXT, 'Click').is_displayed()

def test_button2_clicked(browser):
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    browser.find_element(By.LINK_TEXT, 'Click').click()
    assert browser.find_element(By.ID, 'result-text').text == "Submitted"