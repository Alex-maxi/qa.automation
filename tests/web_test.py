import pytest
from src.application.ui.page_objects.github_login_page import LoginPage


@pytest.mark.web_test
@pytest.mark.negative_test
@pytest.mark.parametrize(
    "username, password",
    [
        ("qa", "qa"),
        ("12345", "12345"), 
        ("", ""), 
        ("qwerty@gmail", "pass"), 
        ("!@#$%^&*()", "!@#$%^&*()")
    ]
)
def test_git_login_page_negative(GitHub_UI_App, username, password):
    login_page = GitHub_UI_App.LoginPage
    login_page.go_to()
    login_page.try_sign_in(username, password)
    login_alert = login_page.check_fail_login_alert()
    assert login_alert, "Login alert not displayed"

@pytest.mark.web_test
@pytest.mark.positive_test
def test_git_login_page_forgot_password_link(GitHub_UI_App):
    login_page = GitHub_UI_App.LoginPage
    login_page.go_to()
    assert login_page.check_forgot_password_link(), "Forgot password link not displayed."

@pytest.mark.web_test
@pytest.mark.positive_test
def test_git_login_page_check_title(GitHub_UI_App):
    login_page = GitHub_UI_App.LoginPage
    login_page.go_to()
    assert login_page.get_title_text() == "Sign in to GitHub"