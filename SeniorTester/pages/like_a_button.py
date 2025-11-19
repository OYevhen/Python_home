from Seniortester.pages.base_page import BasePage
from Seniortester.pages.simple_button import button_selector
from selenium.webdriver.common.by import By

button_selector = (By.LINK_TEXT, 'Click')
result_selector = (By.ID, 'result-text')

class LikeAButton(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://www.qa-practice.com/elements/button/like_a_button')

    @property
    def button(self):
        return self.find(button_selector)

    @property
    def button_is_displayed(self):
        return self.button.is_displayed()

    def button_click(self):
        self.button.click()

    @property
    def result(self):
        return self.find(result_selector)

    @property
    def result_text(self):
        return self.result.text