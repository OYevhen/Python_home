from playwright.sync_api import Page
from base_page import BasePage


class SignUpPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def click_sign_up(self):
        self.page.get_by_role("button", name="Sign Up").click()

    def enter_username(self, username):
        self.page.locator('input[name="name"]').clear()
        self.page.locator('input[name="name"]').fill(username)

    def enter_email(self, email):
        self.page.locator('input[name="email"]').clear()
        self.page.locator('input[name="email"]').fill(email)
    
    def enter_password(self, password):
        self.page.get_by_role("textbox", name="Password", exact=True).fill(password)

    def enter_confirm_password(self, password):
        self.page.get_by_role("textbox", name="Confirm Password").fill(password)

    def username_error_message(self):
        return self._field_error_message("Name")
    
    def email_error_message(self):
        return self._field_error_message("Email")
    
    def password_error_message(self):
        return self._field_error_message("Password")
    
    def confirm_password_error_message(self):
        return self._field_error_message("Confirm Password")

    def _field_error_message(self, field_label: str):
        field = self.page.get_by_role("textbox", name=field_label, exact=True)
        describedby = field.get_attribute("aria-describedby")
        if describedby:
            error_message = self.page.locator(f"#{describedby}")
            error_message.wait_for(state="visible")
            return error_message.text_content()

        error_message = self.page.locator("p.MuiFormHelperText-root.Mui-error").filter(has_text=field_label)
        error_message.wait_for(state="visible")
        return error_message.text_content()
    
    def general_error_message(self):
        error_message = self.page.locator("p.MuiTypography-root.MuiTypography-body1")
        error_message.wait_for(state="visible")
        return error_message.text_content()
    
    def click_toggle_password_visibility(self):
        self.page.get_by_role("button").nth(0).click()

    def click_toggle_confirm_password_visibility(self):
        self.page.get_by_role("button").nth(1).click()