from playwright.sync_api import Page, expect
import pytest

@pytest.mark.skip
def test_login_success(page: Page): 
    page.context.ignore_https_errors = True
    page.goto('https://172.16.6.144')
    
    expect(page.locator('button.button_modal__wrapper--disabled')).to_be_visible(timeout=10000)
    
    page.locator('input[type="text"]').first.fill('user')
    page.locator('input[type="password"]').fill('rds123RDS!@#')
    
    expect(page.get_by_text("Stay signed in")).to_be_visible()

    expect(page.locator('button.button_modal__wrapper--disabled')).to_have_count(0)
    
    page.locator('span.checkbox-custom').click()
    page.locator('span.checkbox-custom').click()
    
    expect(page.locator('button.button_modal__wrapper--disabled')).to_have_count(0)

    page.get_by_role('button', name='Sign in').click()
    
    expect(page.get_by_role('link', name='Dashboard')).to_be_visible(timeout=10000)


def test_login_failed(page: Page):
    pass


def test_logout(page: Page): 
    page.context.ignore_https_errors = True
    page.goto('https://172.16.6.144')
    page.locator('input[type="text"]').first.fill('user')
    page.locator('input[type="password"]').fill('rds123RDS!@#')
    page.get_by_role('button', name='Sign in').click()
    page.get_by_role("button", name="user").click()
    page.get_by_text("Logout").click()
    
    expect(page.get_by_text("Login")).to_be_visible(timeout=10000)