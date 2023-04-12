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
