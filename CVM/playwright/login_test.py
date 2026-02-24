from playwright.sync_api import Page, expect
import pytest
from units import *

#@pytest.mark.skip
def test_login_success(page: Page): 
    page.context.ignore_https_errors = True
    page.goto(URL1)
    
    expect(page.locator('button.button_modal__wrapper--disabled')).to_be_visible(timeout=10000)
    
    page.locator('input[type="text"]').first.fill(username)
    page.locator('input[type="password"]').fill(password)
    
    expect(page.get_by_text("Stay signed in")).to_be_visible()
    expect(page.locator('button.button_modal__wrapper--disabled')).to_have_count(0)
    
    page.locator('span.checkbox-custom').click()
    page.locator('span.checkbox-custom').click()
    
    expect(page.locator('button.button_modal__wrapper--disabled')).to_have_count(0) #Sign in

    page.get_by_role('button', name='Sign in').click()

    expect(page.get_by_text("Authorization...")).to_be_visible()
    expect(page.get_by_role('link', name='Dashboard')).to_be_visible(timeout=10000)


#@pytest.mark.skip(reason="Not implemented yet")
def test_login_failed(page: Page):
    page.context.ignore_https_errors = True
    page.goto(URL1)

    expect(page.locator('button.button_modal__wrapper--disabled')).to_be_visible(timeout=10000)
    
    page.locator('input[type="text"]').first.fill('wrong_user')
    page.locator('input[type="password"]').fill(password)

    page.get_by_role('button', name='Sign in').click()
    expect(page.get_by_text("Authorization...")).to_be_visible()
    expect(page.get_by_text("Invalid password or username")).to_be_visible(timeout=10000)


#@pytest.mark.skip
def test_logout(page: Page): 
    cvm = CVM(page)
    cvm.login(URL1)
    page.get_by_role("button", name="user").click()
    page.get_by_text("Logout").click()
    
    expect(page.get_by_text("Login")).to_be_visible(timeout=10000)