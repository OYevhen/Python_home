from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome()
# browser.implicitly_wait(5)
browser.get("https://rozetka.com.ua/ua/mugskie-botinki/c4634953/")
# browser.implicitly_wait(5)
WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Знайдено'))
# sleep(5)
print('loaded')
shoes = browser.find_elements(By.CLASS_NAME, 'tile-title')
first_shoe = shoes[0]
print(first_shoe.id)
print(first_shoe.text)
print(first_shoe.get_attribute('href'))
sorter = browser.find_element(By.ID, 'sort')
select = Select(sorter)
select.select_by_value('cheap')
# browser.implicitly_wait(5)
WebDriverWait(browser, 10).until(EC.staleness_of(first_shoe))
shoes = browser.find_elements(By.CLASS_NAME, 'tile-title')
first_shoe = shoes[0]
print(first_shoe.text)
print(first_shoe.get_attribute('href'))