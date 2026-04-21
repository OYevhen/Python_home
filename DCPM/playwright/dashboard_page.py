from playwright.sync_api import Page
from base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_profile_menu(self):
        self.page.get_by_role("img").nth(3).click()

    def click_sign_out_menu_item(self):
        self.page.get_by_role("menuitem", name="Sign Out").click()

    def confirm_sign_out(self):
        self.page.get_by_role("button", name="Sign Out").click()

    def sign_out(self):
        self.open_profile_menu()
        self.click_sign_out_menu_item()
        self.confirm_sign_out()
        self.wait_for_load()