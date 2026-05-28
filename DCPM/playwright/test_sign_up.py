from playwright.sync_api._generated import Page
import pytest

from sign_up_page import SignUpPage
from units import URL, username, password

def test_t17(browser_context: Page):
    """"All required fields display error on empty submission"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_email("test@datacore.com")
    sign_up_page.enter_password(password)
    sign_up_page.enter_confirm_password(password)
    sign_up_page.click_sign_up()

    assert sign_up_page.username_error_message() == "Username must be at least 3 characters"

    sign_up_page.enter_username("test")
    sign_up_page.enter_email("")
    sign_up_page.click_sign_up()

    assert sign_up_page.email_error_message() == "Invalid email"

    sign_up_page.enter_email("test@datacore.com")
    sign_up_page.enter_password("")
    sign_up_page.click_sign_up()

    assert sign_up_page.password_error_message() == "Password must be at least 8 characters"
    assert sign_up_page.confirm_password_error_message() == "Passwords do not match"

    sign_up_page.enter_confirm_password("")
    sign_up_page.click_sign_up()

    assert sign_up_page.confirm_password_error_message() == "Required"


def test_t67(browser_context: Page):
    """Confirm Password visibility toggles with eye icon"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_confirm_password(password)
    confirm_password_field = page.get_by_role("textbox", name="Confirm Password")
    
    assert confirm_password_field.get_attribute("type") == "password"

    sign_up_page.click_toggle_confirm_password_visibility()

    assert confirm_password_field.get_attribute("type") == "text"

    sign_up_page.click_toggle_confirm_password_visibility()

    assert confirm_password_field.get_attribute("type") == "password"


def test_t18(browser_context: Page):
    """Error message appears on invalid email input"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_email("invalid-email")
    sign_up_page.click_sign_up()

    assert sign_up_page.email_error_message() == "Invalid email"


def test_t68(browser_context: Page):
    """Error message appears when Confirm Password field is empty"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_confirm_password("")
    sign_up_page.click_sign_up()

    assert sign_up_page.confirm_password_error_message() == "Required"


def test_t66(browser_context: Page):
    """Error message appears when Confirm Passwords do not match"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_password(password)
    sign_up_page.enter_confirm_password("differentPassword")
    sign_up_page.click_sign_up()

    assert sign_up_page.confirm_password_error_message() == "Passwords do not match"


def test_t37(browser_context: Page):
    """Error message appears when email already exists"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("newuser")
    sign_up_page.enter_email("existing@datacore.com")
    sign_up_page.enter_password(password)
    sign_up_page.enter_confirm_password(password)
    sign_up_page.click_sign_up()

    assert sign_up_page.general_error_message() == "Email is already taken"


def test_t39(browser_context: Page):
    """Error message appears when email format is invalid"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("newuser1")
    sign_up_page.enter_email("yruyfuysadyruyfuysadasdaseqeqeqeqeqweeweweweweweweweqeqweqweqwedasdadadasufysfsfyruyfuysadasdaseqeqeqeqeqweeweweweweweweweqeqweqweqwedasdadadasufysfsfyruyfuysadasdaseqeqeqeqeqweeweweweweweweweqeqweqweqwedasdadadasufysfsfyruyfuysadasdaseqeqeqeqeqweewewdfddasdaseqeqeqeqeqweeweweweweweweweqeqweqweqwedasdadadasufysfsf@dadsadas.comdadadadadadsasdasdasdadas")
    sign_up_page.enter_password(password)
    sign_up_page.enter_confirm_password(password)
    sign_up_page.click_sign_up()

    assert sign_up_page.general_error_message() == "email must be an email"


def test_t29(browser_context: Page):
    """Error message appears when Password do not match"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("newuser2")
    sign_up_page.enter_email("newuser2@datacore.com")
    sign_up_page.enter_password(password)
    sign_up_page.enter_confirm_password("DifferentPassword")
    sign_up_page.click_sign_up()

    assert sign_up_page.confirm_password_error_message() == "Passwords do not match"


def test_t28(browser_context: Page):
    """Error message appears when Password field is empty"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("newuser3")
    sign_up_page.enter_email("newuser3@datacore.com")
    sign_up_page.enter_password("")
    sign_up_page.enter_confirm_password("")
    sign_up_page.click_sign_up()

    assert sign_up_page.password_error_message() == "Password must be at least 8 characters"



def test_t65(browser_context: Page):
    """Error message appears when username already exists"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("user")
    sign_up_page.enter_email("existing@datacore.com")
    sign_up_page.enter_password(password)
    sign_up_page.enter_confirm_password(password)
    sign_up_page.click_sign_up()

    assert sign_up_page.general_error_message() == "Name is already taken"


@pytest.mark.skip(reason="Not implemented yet")
def test_t32(browser_context: Page):
    """Password accepts Latin alphabet characters only"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("ab")
    sign_up_page.enter_email("newuser@datacore.com")
    sign_up_page.enter_password("квы123КВЫ!")
    sign_up_page.enter_confirm_password("квы123КВЫ!")
    sign_up_page.click_sign_up()

    assert sign_up_page.password_error_message() == "Password must use Latin characters only"


def test_t22(browser_context: Page):
    """Password does not exceed maximum length limit"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("ab")
    sign_up_page.enter_email("newuser@datacore.com")
    sign_up_page.enter_password("qwertyA1!uiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuioplkjhgfdsazxcvbnmnbvcxzlkjhgfdsaqwertyq")
    sign_up_page.enter_confirm_password("qwertyA1!uiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuioplkjhgfdsazxcvbnmnbvcxzlkjhgfdsaqwertyq")
    sign_up_page.click_sign_up()

    assert sign_up_page.password_error_message() == "Password must be at most 128 characters"


def test_t30(browser_context: Page):
    """Password is masked by default on Sign Up page"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_password("Password123")
    password_field = page.get_by_role("textbox", name="Password", exact=True)

    assert password_field.get_attribute("type") == "password"


def test_t21(browser_context: Page):
    """Password meets minimum length requirement"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username(username)
    sign_up_page.enter_password("​rds")

    assert sign_up_page.password_error_message() == "Password must be at least 8 characters"


def test_t27(browser_context: Page):
    """Password rejects spaces"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("testuser")
    sign_up_page.enter_password("rds123RDS !")

    assert sign_up_page.password_error_message() == "Password cannot contain spaces"


def test_t24(browser_context: Page):
    """Password requires at least one lowercase letter"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("testuser")
    sign_up_page.enter_password("RDS!@#RDS123")

    assert sign_up_page.password_error_message() == "Password must contain at least one lowercase letter"


def test_t25(browser_context: Page):
    """Password requires at least one numeric character"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("testuser")
    sign_up_page.enter_password("rdsRDS!@#")

    assert sign_up_page.password_error_message() == "Password must contain at least one number"


def test_t26(browser_context: Page):
    """Password requires at least one numeric character"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("testuser")
    sign_up_page.enter_password("rds123RDS")

    assert sign_up_page.password_error_message() == "Password must contain at least one special character"


def test_t23(browser_context: Page):
    """Password requires at least one numeric character"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("testuser")
    sign_up_page.enter_password("rds123rds!")

    assert sign_up_page.password_error_message() == "Password must contain at least one uppercase letter"


def test_t34(browser_context: Page):
    """Confirm Password visibility toggles with eye icon"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_password(password)
    confirm_password_field = page.get_by_role("textbox", name="Password", exact=True)
    
    assert confirm_password_field.get_attribute("type") == "password"

    sign_up_page.click_toggle_password_visibility()

    assert confirm_password_field.get_attribute("type") == "text"

    sign_up_page.click_toggle_password_visibility()

    assert confirm_password_field.get_attribute("type") == "password"


def test_t13(browser_context: Page):
    """Sign Up page displays all required elements"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)

    assert page.get_by_role("textbox", name="Name").is_visible()
    assert page.get_by_role("textbox", name="Email").is_visible()
    assert page.get_by_role("textbox", name="Password", exact=True).is_visible()
    page.get_by_role("textbox", name="Confirm Password", exact=True).wait_for(state="visible")
    assert page.get_by_role("textbox", name="Confirm Password", exact=True).is_visible()
    assert page.get_by_role("button", name="Sign Up").is_visible()
    assert page.get_by_role("button").nth(0).is_visible()
    assert page.get_by_role("button").nth(1).is_visible()
    assert page.get_by_text("Already have an account?").is_visible()
    assert page.get_by_role("link", name="Sign In").is_visible()


def test_t3(browser_context: Page):
    """Space at the beginning of the Username is ignored"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username(" testuser")
    sign_up_page.enter_email("test@domain.com")
    assert page.get_by_role("paragraph", name="Name").is_not_visible()


def test_t43(browser_context: Page):
    """User is registered successfully when all fields are valid"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("user43")
    sign_up_page.enter_email("test43@domain.com")
    sign_up_page.enter_password("RDS!@#RDS123")
    sign_up_page.enter_confirm_password("RDS!@#RDS123")
    sign_up_page.click_sign_up()
    
    assert "DataCore Platform" in page.title()


def test_t15(browser_context: Page):
    """Username does not exceed maximum length limit"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("a" * 51)

    assert sign_up_page.username_error_message() == "Username must be at most 50 characters"


def test_t14(browser_context: Page):
    """Username meets minimum length requirement"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("a" * 2)

    assert sign_up_page.username_error_message() == "Username must be at least 3 characters"


@pytest.mark.skip(reason="Not implemented yet")
def test_t62(browser_context: Page):
    """Username must end with a letter or number"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("user_")

    assert sign_up_page.username_error_message() == "Username must end with a letter or number"


@pytest.mark.skip(reason="Not implemented yet")
def test_t19(browser_context: Page):
    """Username must start with a letter"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("User")

    assert sign_up_page.username_error_message() == "Must begin with a letter (a-z)"

    sign_up_page.enter_username("1user")

    assert sign_up_page.username_error_message() == "Must begin with a letter (a-z)"


@pytest.mark.skip(reason="Not implemented yet")
def test_t20(browser_context: Page):
    """Username rejects consecutive special characters"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username("user__name")

    assert sign_up_page.username_error_message() == "Cannot contain two or more special characters in a row"


@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("name", ["admin", "root", "system", "support", "api", "localhost", "bin", "guest", "superadmin", "help", "contact", "info"])
def test_t64(browser_context: Page, name: str):
    """Username rejects reserved names"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username(name)

    assert sign_up_page.username_error_message() == "Reserved name"


@pytest.mark.parametrize("symbol", ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", "|", "\\", "/", "<", ">", "~"])
def test_t16(browser_context: Page, symbol: str):
    """Username rejects special characters"""
    page = browser_context
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_sign_up(URL)
    sign_up_page.enter_username(f"user{symbol}name")

    assert sign_up_page.username_error_message() == "Username may contain only letters, numbers, hyphens, underscores, and periods"


