import time
from SeniorTester.pages.homepage import HomePage
from SeniorTester.pages.product import ProductPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    #driver.get("https://www.demoblaze.com")
    #galaxy_s6 = driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    #galaxy_s6 = driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    #galaxy_s6.click()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')
    #title = driver.find_element(By.CSS_SELECTOR, 'h2')
    #assert title.text == 'Samsung galaxy s6'

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    #driver.get("https://www.demoblaze.com")
    homepage.click_monitor()
    #monitors_link = driver.find_element(By.CSS_SELECTOR, '''onclick="byCat('monitor')"''')
    #monitors_link.click()
    time.sleep(20)
    homepage.check_products_count(2)
    # monitors = driver.find_elements(By.CSS_SELECTOR, ".card")
    # assert len(monitors) == 2