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
#         sign_in_page.enter_username()
#         sign_in_page.enter_password("rds123RDS!@#")  
#         sign_in_page.click_sign_in()
#     account_locked_message = page.get_by_text("Account locked")
    
#     assert account_locked_message.is_visible()


def test_t81(browser_context: Page):
    """Error message appears on unauthorized sign in attempt"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username("resu") # Incorrect username
    sign_in_page.enter_password()
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.general_error_message()
    expected_text = "Invalid credentials"

    assert actual_text == expected_text


def test_t49(browser_context: Page):
    """Failed attempt counter resets after successful login"""
    page = browser_context
    sign_in_page = SignInPage(page)
    dashboard_page = DashboardPage(page)
    sign_in_page.navigate_to(URL)
    for _ in range(4):
        sign_in_page.enter_username()
        sign_in_page.enter_password("rds123RDS!@#")
        sign_in_page.click_sign_in()
    sign_in_page.enter_password()
    sign_in_page.click_sign_in()
    dashboard_page.sign_out()
    # sign_in_page.navigate_to(URL)
    for _ in range(4):
        sign_in_page.enter_username()
        sign_in_page.enter_password("rds123RDS!@#")
        sign_in_page.click_sign_in()
    sign_in_page.enter_username()
    sign_in_page.enter_password()
    sign_in_page.click_sign_in()
    account_locked_message = page.get_by_text("Account locked")
    
    assert not account_locked_message.is_visible()

@pytest.mark.skip(reason="Not implemented yet")
def test_t61(browser_context: Page):
    """Password accepts Latin alphabet characters only"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username()
    sign_in_page.enter_password("пароль")
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.password_error_message()
    expected_text = "INSERT APPROPRIATE ERROR MESSAGE"
    
    assert actual_text == expected_text


def test_t55(browser_context: Page):
    """Password does not exceed maximum length limit"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username()
    sign_in_page.enter_password("rds123RDS!@#" * 11)
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.password_error_message()
    expected_text = "Password must be at most 128 characters"

    assert actual_text == expected_text


def test_t31(browser_context: Page):  
    """Password is masked by default on Sign In page"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    password_field = page.get_by_role("textbox", name="Password")
    sign_in_page.enter_password()    
    password_field = page.get_by_role("textbox", name="Password")
   
    assert password_field.get_attribute("type") == "password"


def test_t5(browser_context: Page):
    """Password meets minimum length requirement"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username()
    sign_in_page.enter_password("rd12R!@")
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.password_error_message()
    expected_text = "Password must be at least 8 characters"
    
    assert actual_text == expected_text


@pytest.mark.skip(reason="Not implemented yet")
def test_t58(browser_context: Page):
    """Password requires at least one digit"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username()
    sign_in_page.enter_password("rdsRDS!@#")
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.password_error_message()
    expected_text = "Password must contain at least one digit"
    
    assert actual_text == expected_text



def test_t57(browser_context: Page):
    """Password requires at least one lowercase letter"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username()
    sign_in_page.enter_password("RDS!@#RDS123")
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.password_error_message()
    expected_text = "Password must contain at least one lowercase letter"
    
    assert actual_text == expected_text


def test_t60(browser_context: Page):
    """Password requires at least one special character"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username()
    sign_in_page.enter_password("rds123RDS")
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.password_error_message()
    expected_text = "Password must contain at least one special character"

    assert actual_text == expected_text


def test_t56(browser_context: Page):
    """Password requires at least one uppercase letter"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username()
    sign_in_page.enter_password("rds!@#rds123")
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.password_error_message()
    expected_text = "Password must contain at least one uppercase letter"

    assert actual_text == expected_text


def test_t7(browser_context: Page):
    """Password visibility toggles with eye icon"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_password()
    password_field = page.get_by_role("textbox", name="Password")
    
    assert password_field.get_attribute("type") == "password"

    sign_in_page.click_toggle_password_visibility()

    assert password_field.get_attribute("type") == "text"

    sign_in_page.click_toggle_password_visibility()

    assert password_field.get_attribute("type") == "password"


def test_t85(browser_context: Page):
    """Sign In is rejected and error message appears when password field is empty"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username()
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.password_error_message()
    expected_text = "Password must be at least 8 characters"

    assert actual_text == expected_text


def test_t69(browser_context: Page):
    """Sign In is rejected and error messages appear when all fields are empty"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.click_sign_in()

    actual_text1 = sign_in_page.username_error_message()
    expected_text1 = "Enter a valid email or username (letters, numbers, hyphens, underscores, periods; 3–50 chars)"
    actual_text2 = sign_in_page.password_error_message()
    expected_text2 = "Password must be at least 8 characters"

    assert actual_text1 == expected_text1
    assert actual_text2 == expected_text2


def test_t1(browser_context: Page):
    """Sign In page displays all required elements"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    username_field = page.get_by_role("textbox", name="Name or Email")
    password_field = page.get_by_role("textbox", name="Password")
    stay_signed_in_checkbox = page.get_by_role("checkbox", name="Stay signed in")
    sign_in_button = page.get_by_role("button", name="Sign In")

    assert username_field.is_visible()
    assert password_field.is_visible()
    assert stay_signed_in_checkbox.is_visible()
    assert sign_in_button.is_visible()


def test_t2(browser_context: Page):
    """User is redirected to dashboard after successful sign in"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.sign_in()
    
    assert "DataCore Platform" in page.title()


def test_t83(browser_context: Page):
    """User is redirected to sign-in page after successful sign out"""
    page = browser_context
    sign_in_page = SignInPage(page)
    dashboard_page = DashboardPage(page)
    sign_in_page.sign_in()
    dashboard_page.sign_out()
    
    assert "DataCore Platform" in page.title()


@pytest.mark.skip(reason="Not implemented yet")
def test_t54(browser_context: Page):
    """Username accepts Latin alphabet characters only"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username("юзернейм")
    sign_in_page.enter_password()
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.username_error_message()
    expected_text = "INSERT APPROPRIATE ERROR MESSAGE"

    assert actual_text == expected_text


def test_t53(browser_context: Page):
    """Username accepts only allowed characters"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username("user!name")
    sign_in_page.enter_password()
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.username_error_message()
    expected_text = "Enter a valid email or username (letters, numbers, hyphens, underscores, periods; 3–50 chars)"

    assert actual_text == expected_text

@pytest.mark.skip(reason="Not implemented yet")
def test_t52(browser_context: Page):
    """Username does not exceed maximum length limit"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username("u" * 51)
    sign_in_page.enter_password()
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.username_error_message()
    expected_text = "Username must be at most 50 characters"

    assert actual_text == expected_text


def test_t84(browser_context: Page):
    """Username is case-insensitive"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username(username.upper())
    sign_in_page.enter_password()
    sign_in_page.click_sign_in()    
    actual_text = sign_in_page.general_error_message()
    expected_text = "Invalid credentials"

    assert actual_text == expected_text


@pytest.mark.skip(reason="Not implemented yet")
def test_t51(browser_context: Page):
    """Username meets minimum length requirement"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username("us")
    sign_in_page.enter_password()
    sign_in_page.click_sign_in()
    actual_text = sign_in_page.username_error_message()
    expected_text = "Username must be at least 3 characters"

    assert actual_text == expected_text


def test_t59(browser_context: Page):
    """Username/Password rejects spaces"""
    page = browser_context
    sign_in_page = SignInPage(page)
    sign_in_page.navigate_to(URL)
    sign_in_page.enter_username("user name")
    sign_in_page.enter_password("rds123 RDS!@#")
    sign_in_page.click_sign_in()
    actual_text1 = sign_in_page.username_error_message()
    expected_text1 = "Enter a valid email or username (letters, numbers, hyphens, underscores, periods; 3–50 chars)"
    actual_text2 = sign_in_page.password_error_message()
    expected_text2 = "Password cannot contain spaces"   

    assert actual_text1 == expected_text1
    assert actual_text2 == expected_text2