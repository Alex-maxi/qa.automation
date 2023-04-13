import pytest
from src.application.ui.page_objects.github_login_page import LoginPage


@pytest.mark.web_test
@pytest.mark.negative_test
@pytest.mark.parametrize(
    "username, password",
    [
        ("qa", "qa"),
        ("12345", "12345"), 
        (" ", " "), 
        ("qwerty@gmail", "pass"), 
        ("!@#$%^&*()", "!@#$%^&*()")
    ]
)
def test_git_login_page_negative(driver, username, password):
    login_page = LoginPage(driver)
    login_page._open()
    login_alert = (
        login_page.enter_user_name(username)
        .enter_password(password)
        .press_sign_in_button()
        .assertion_fail_check()
    )
    assert login_alert, "Login alert not displayed"

@pytest.mark.web_test
@pytest.mark.positive_test
def test_git_login_page_forgot_password_link(driver):
    login_page = LoginPage(driver)
    login_page._open()
    assert login_page.forgot_password_link_check(), "Forgot password link not displayed."

@pytest.mark.web_test
@pytest.mark.positive_test
def test_git_login_page_forgot_password_link(driver):
    login_page = LoginPage(driver)
    login_page._open()
    assert login_page.title_check_text() == "Sign in to GitHub"