from playwright.sync_api import Page
from base_page import BasePage
from units import URL, username, password


class SignInPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def enter_username(self, username: str):
        self.page.get_by_role("textbox", name="Name or Email").fill(username)

    def enter_password(self, password: str):
        self.page.get_by_role("textbox", name="Password").fill(password)

    def click_sign_in(self):
        self.page.get_by_role("button", name="Sign In").click()

    def sign_in(self):
        self.navigate_to(URL)
        self.enter_username(username)
        self.enter_password(password)
        self.click_sign_in()
        self.wait_for_load()