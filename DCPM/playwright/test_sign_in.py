from playwright.sync_api._generated import Page
import pytest

from sign_in_page import SignInPage
from dashboard_page import DashboardPage
from units import URL, username, password


def test_t8(browser_context: Page):
    """"Stay signed in" checkbox is clickable and changes state"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    checkbox = page.get_by_role("checkbox", name="Stay signed in")
    
    assert not checkbox.is_checked()
    
    checkbox.click()
    
    assert checkbox.is_checked()


# def test_t50(browser_context: Page):
#     """Account is locked after 6 unsuccessful login attempts"""
#     page = browser_context
#     sign_in_page = SignInPage(page)
#     sign_in_page.navigate_to(URL)
#     for _ in range(6):
#         sign_in_page.enter_username(username)
#         sign_in_page.enter_password("rds123RDS!@#")  # Incorrect password
#         sign_in_page.click_sign_in()
#     account_locked_message = page.get_by_text("Account locked")
    
#     assert account_locked_message.is_visible()


def test_t81(browser_context: Page):
    """Error message appears on unauthorized sign in attempt"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username("resu") # Incorrect username
    sign_in_page.enter_password(password)
    sign_in_page.click_sign_in()
    error_message = page.get_by_text("Invalid credentials")
    error_message.wait_for(state="visible")
    
    assert error_message.is_visible()


def test_t4(browser_context: Page):
    """Error message appears when Username/Password fields are empty"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.click_sign_in()
    error_message1 = page.get_by_text("Enter a valid email or username (letters, numbers, hyphens, underscores, periods; 3–50 chars)")
    error_message1.wait_for(state="visible")
    error_message2 = page.get_by_text("Password must be at least 8 characters")

    assert error_message1.is_visible()
    assert error_message2.is_visible()

    sign_in_page.enter_username(username)
    sign_in_page.click_sign_in()
    error_message1.wait_for(state="hidden")

    assert not error_message1.is_visible()

    sign_in_page.enter_password(password)
    sign_in_page.click_sign_in()
    error_message2.wait_for(state="hidden")

    assert not error_message2.is_visible()


def test_t49(browser_context: Page):
    """Failed attempt counter resets after successful login"""
    page = browser_context
    sign_in_page = SignInPage(page)
    dashboard_page = DashboardPage(page)
    sign_in_page.navigate_to(URL)
    for _ in range(4):
        sign_in_page.enter_username(username)
        sign_in_page.enter_password("rds123RDS!@#")  # Incorrect password
        sign_in_page.click_sign_in()
    sign_in_page.enter_password(password)
    sign_in_page.click_sign_in()
    dashboard_page.sign_out()
    # sign_in_page.navigate_to(URL)
    for _ in range(4):
        sign_in_page.enter_username(username)
        sign_in_page.enter_password("rds123RDS!@#")  # Incorrect password
        sign_in_page.click_sign_in()
    sign_in_page.enter_username(username)
    sign_in_page.enter_password(password)
    sign_in_page.click_sign_in()
    account_locked_message = page.get_by_text("Account locked")
    
    assert not account_locked_message.is_visible()

@pytest.mark.skip(reason="Not implemented yet")
def test_t61(browser_context: Page):
    """Password accepts Latin alphabet characters only"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username(username)
    sign_in_page.enter_password("пароль")  # Password in Cyrillic
    sign_in_page.click_sign_in()
    error_message = page.get_by_text("INSERT APPROPRIATE ERROR MESSAGE")
    error_message.wait_for(state="visible")
    
    assert error_message.is_visible()


def test_t55(browser_context: Page):
    """Password does not exceed maximum length limit"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username(username)
    sign_in_page.enter_password("rds123RDS!@#" * 11)  # Password exceeds maximum length
    sign_in_page.click_sign_in()
    error_message = page.get_by_text("Password must be at most 128 characters")
    error_message.wait_for(state="visible")

    assert error_message.is_visible()


def test_t5(browser_context: Page):
    """Password meets minimum length requirement"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username(username)
    sign_in_page.enter_password("rd12R!@")  # Password meets minimum length
    sign_in_page.click_sign_in()
    error_message = page.get_by_text("Password must be at least 8 characters")
    
    assert error_message.is_visible()


def test_t57(browser_context: Page):
    """Password requires at least one lowercase letter"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username(username)
    sign_in_page.enter_password("RDS!@#RDS123")  # Password without lowercase letters
    sign_in_page.click_sign_in()
    error_message = page.get_by_text("Password must contain at least one lowercase letter")
    error_message.wait_for(state="visible") 

    assert error_message.is_visible()


def test_t83(browser_context: Page):
    """User is redirected to sign-in page after successful sign out"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.click_sign_in()
    error_message = page.get_by_text("Username and password are required")
    error_message.wait_for(state="visible")

    assert error_message.is_visible()


def test_t83(browser_context: Page):
    """User is redirected to sign-in page after successful sign out"""
    page = browser_context
    sign_in_page = SignInPage(page)
    dashboard_page = DashboardPage(page)
    sign_in_page.sign_in()
    dashboard_page.sign_out()
    
    assert "DataCore Platform" in page.title()