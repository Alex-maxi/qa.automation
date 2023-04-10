
import pytest
from src.application.ui.page_objects.login_page import LoginPage
from src.config.config import config

base_url = config.get('BASE_URL_UI')


@pytest.mark.web_test
@pytest.mark.negative
@pytest.mark.parametrize("username, password", [("qa", "qa"), ("12345", "12345"), (" ", " "), ("qwerty@gmail", "pass"), ("!@#$%^&*()", "!@#$%^&*()")])
def test_git_login_page_negative(driver, username, password):
    profile_page = LoginPage(driver, f'{base_url}/login')
    profile_page.open()
    login_alert = (profile_page
                   .enter_user_name(username)
                   .enter_password(password)
                   .press_sign_in_button()
                   .assertion_fail_check())
    assert login_alert == True


