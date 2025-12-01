from selenium import webdriver
from selenium.webdriver.common.by import By
import dotenv
dotenv.load_dotenv()
import os

def browser():
    browser = webdriver.Firefox
    return browser

def test_request(browser):
    browser.get("https://google.com")
    search = os.getenv('G_REQ')
    browser.find_element(By.NAME, 'q').send_keys(search)
