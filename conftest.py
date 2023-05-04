"""The `pytest` module provides a testing framework for Python"""
import pytest
from src.providers.service.browsers.browsers_provider import BrowsersProvider
from src.application.api.github_api_client import GitHubApiClient
from src.application.ui.github_ui_app import GitHubUI
from src.config.config import CONFIG

from src.data.models.users import User


@pytest.fixture(scope="function")
def user_class():
    """
    Test fixture for User Class. Not used yet.
    """
    # before test
    print("Create user")
    user = User(43, "Alex")

    # pass user object to test
    yield user

    # after test
    print("Remove user")
    user.remove()

@pytest.fixture(scope="session")
def github_api_client():
    """
    Fixture which returns authorized github api client.
    """
    api_client = GitHubApiClient()
    api_client.login()

    yield api_client

    api_client.logout()


@pytest.fixture(scope="function")
def git_hub_ui_app():
    """
    Fixture which returns browser(driver) from 'BrowsersProvider' Class 
    to UI App and then to Page Object models.
    """
    # before test

    browser = CONFIG.get("BROWSER")
    browser = BrowsersProvider.get_driver(browser)

    ui_app = GitHubUI(browser)

    # pass driver(WebDriver) object to test
    yield ui_app

    # after test
    ui_app.close()
