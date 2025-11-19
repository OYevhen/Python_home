from selenium.webdriver.common.by import By


def test_button1_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()

def test_button1_clicked(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    browser.find_element(By.ID, 'submit-id-submit').click()
    assert browser.find_element(By.ID, 'result-text').text == "Submitted"