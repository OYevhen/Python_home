from selenium.webdriver.common.by import By
import time


def test_open_s6(driver):
    driver.get("https://www.demoblaze.com")
    #galaxy_s6 = driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    galaxy_s6 = driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    galaxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'

def test_two_monitors(driver):
    driver.get("https://www.demoblaze.com")
    monitors_link = driver.find_element(By.CSS_SELECTOR, '''onclick="byCat('monitor')"''')
    monitors_link.click()
    time.sleep(3)
    monitors = driver.find_elements(By.CSS_SELECTOR, ".card")
    assert len(monitors) == 2