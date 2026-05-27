from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_sign_in(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def navigate_to_sign_up(self, url: str):
        self.page.goto(url)
        # self.page.wait_for_load_state("networkidle")
        self.page.get_by_role("link", name="Sign Up").click()
        # self.page.wait_for_load_state("networkidle")


    def get_title(self) -> str:
        return self.page.title()

