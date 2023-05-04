"""The `pytest` module provides a testing framework for Python"""
import pytest


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
def test_git_login_page_negative(git_hub_ui_app, username, password):
    """
    Negative test with incorrect credentials.
    Args:
        git_hub_ui_app (function): Fixture which returns browser(driver) 
        from 'BrowsersProvider' Class to UI App and then to Page Object models.
        username (_type_): parametrize data
        password (_type_): parametrize data
    """
    login_page = git_hub_ui_app.login_page
    login_page.go_to()
    login_page.try_sign_in(username, password)
    login_alert = login_page.check_fail_login_alert()

    assert login_alert, "Login alert not displayed"


@pytest.mark.web_test
@pytest.mark.positive_test
def test_git_login_page_forgot_password_link(git_hub_ui_app):
    """
    Checking forgot password link
    Args:
        git_hub_ui_app (function): Fixture which returns browser(driver) 
        from 'BrowsersProvider' Class to UI App and then to Page Object models.
    """
    login_page = git_hub_ui_app.login_page
    login_page.go_to()

    assert login_page.check_forgot_password_link(), "Forgot password link not displayed."


@pytest.mark.web_test
@pytest.mark.positive_test
def test_git_login_page_check_title(git_hub_ui_app):
    """
    Checking title of page
    Args:
        git_hub_ui_app (function): Fixture which returns browser(driver) 
        from 'BrowsersProvider' Class to UI App and then to Page Object models.
    """
    login_page = git_hub_ui_app.login_page
    login_page.go_to()

    assert login_page.get_login_page_title_text() == "Sign in to GitHub · GitHub"


@pytest.mark.web_test
@pytest.mark.positive_test
def test_link_signup_page(git_hub_ui_app):
    """
    Checking link to signup page
    Args:
        git_hub_ui_app (function): Fixture which returns browser(driver) 
        from 'BrowsersProvider' Class to UI App and then to Page Object models.
    """
    login_page = git_hub_ui_app.login_page
    login_page.go_to().go_to_signup_page()

    signup_page_title = login_page.get_title()
    signup_page_url = login_page.get_url()

    assert (signup_page_url == "https://github.com/signup?source=login" and
            signup_page_title == "Join GitHub · GitHub")


@pytest.mark.web_test
@pytest.mark.positive_test
def test_link_password_reset_page(git_hub_ui_app):
    """
    Checking link to password reset page
    Args:
        git_hub_ui_app (function): Fixture which returns browser(driver) 
        from 'BrowsersProvider' Class to UI App and then to Page Object models.
    """
    login_page = git_hub_ui_app.login_page
    login_page.go_to().go_to_password_reset_page()

    reset_page_title = login_page.get_title()
    reset_page_url = login_page.get_url()

    assert (reset_page_url == "https://github.com/password_reset" and
            reset_page_title == "Forgot your password? · GitHub")


@pytest.mark.web_test
@pytest.mark.positive_test
def test_link_terms_page(git_hub_ui_app):
    """
    Checking link to terms page
    Args:
        git_hub_ui_app (function): Fixture which returns browser(driver) 
        from 'BrowsersProvider' Class to UI App and then to Page Object models.
    """
    login_page = git_hub_ui_app.login_page
    login_page.go_to().go_to_terms_page()

    terms_page_title = login_page.get_title()
    terms_page_url = login_page.get_url()

    assert (terms_page_url == "https://docs.github.com/en/site-policy/github-terms/github-terms-of-service" and
            terms_page_title == "GitHub Terms of Service - GitHub Docs")


@pytest.mark.web_test
@pytest.mark.positive_test
def test_link_privacy_page(git_hub_ui_app):
    """
    Checking link to privacy page
    Args:
        git_hub_ui_app (function): Fixture which returns browser(driver) 
        from 'BrowsersProvider' Class to UI App and then to Page Object models.
    """
    login_page = git_hub_ui_app.login_page
    login_page.go_to().go_to_privacy_page()

    privacy_page_title = login_page.get_title()
    privacy_page_url = login_page.get_url()

    assert (privacy_page_url == "https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" and
            privacy_page_title == "GitHub Privacy Statement - GitHub Docs")


@pytest.mark.web_test
@pytest.mark.positive_test
def test_link_security_page(git_hub_ui_app):
    """
    Checking link to security page
    Args:
        git_hub_ui_app (function): Fixture which returns browser(driver) 
        from 'BrowsersProvider' Class to UI App and then to Page Object models.
    """
    login_page = git_hub_ui_app.login_page
    login_page.go_to().go_to_security_page()

    security_page_title = login_page.get_title()
    security_page_url = login_page.get_url()

    assert (security_page_url == "https://github.com/security" and
            security_page_title == "GitHub Security · GitHub")


@pytest.mark.web_test
@pytest.mark.positive_test
def test_link_support_page(git_hub_ui_app):
    """
    Checking link to support page
    Args:
        git_hub_ui_app (function): Fixture which returns browser(driver) 
        from 'BrowsersProvider' Class to UI App and then to Page Object models.
    """
    login_page = git_hub_ui_app.login_page
    login_page.go_to().go_to_github_support_page()

    support_page_title = login_page.get_title()
    support_page_url = login_page.get_url()

    assert (support_page_url == "https://support.github.com/?tags=dotcom-direct" and
            support_page_title == "GitHub Support")
