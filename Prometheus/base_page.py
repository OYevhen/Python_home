from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BasePage:
    PATH = r"C:/Users/orely/PycharmProjects/Python_home/Prometheus"
    DRIVER_NAME = "chrome driver"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()