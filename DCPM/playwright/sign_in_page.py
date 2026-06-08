from playwright.sync_api import Page
from base_page import BasePage
from units import URL, username, password


class SignInPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def navigate_to(self, url=URL):
        self.page.goto(url)

    def enter_username(self, username=username):
        self.page.locator('input[name="identifier"]').clear()
        self.page.locator('input[name="identifier"]').fill(username)

    def enter_password(self, password=password):
        self.page.get_by_role("textbox", name="Password").fill(password)

    def click_toggle_password_visibility(self):
        self.page.locator("button.MuiIconButton-root").click()

    def click_sign_in(self):
        self.page.get_by_role("button", name="Sign In").click()

    def sign_in(self):
        self.navigate_to(URL)
        self.enter_username()
        self.enter_password()
        self.click_sign_in()
        self.wait_for_load()

    def general_error_message(self):
        error_message = self.page.locator("p.MuiTypography-root.MuiTypography-body1").filter(has_text="Invalid")
        error_message.wait_for(state="visible")
        return error_message.text_content()    

    def username_error_message(self):
        error_message = self.page.locator("p.MuiFormHelperText-root.Mui-error").filter(has_text="email or username")
        error_message.wait_for(state="visible")
        return error_message.text_content()

    def password_error_message(self):
        error_message = self.page.locator("p.MuiFormHelperText-root.Mui-error").filter(has_text="Password")
        error_message.wait_for(state="visible")
        return error_message.text_content()

