import pytest
from playwright.sync_api import Playwright, Browser, Page


@pytest.fixture(scope="function")
def browser_context(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    # browser = playwright.firefox.launch(headless=False)
    # browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()