from sign_in_page import SignInPage
import pytest

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # Створення обьєкту сторінки
    sign_in_page = SignInPage()

    # відкриваємо сторінку
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему
    sign_in_page.try_login("test", "wrong password")

    # перевіряємо що назва сторінки така, яку очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # закриваємо браузер
    sign_in_page.close()