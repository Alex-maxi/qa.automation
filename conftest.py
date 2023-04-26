import pytest
from src.providers.service.browsers.browsers_provider import BrowsersProvider
from src.application.api.github_api_client import GitHubApiClient
from src.application.ui.github_ui_app import GitHubUI
from src.config.config import CONFIG

from src.data.models.users import User


@pytest.fixture(scope="function")
def user():
    # before test
    print("Create user")
    user = User(43, "Alex")

    # pass user object to test
    yield user

    # after test
    print("Remove user")
    user.remove()

@pytest.fixture(scope="session")
def GitHub_Api_Client():
    github_api_client = GitHubApiClient()
    github_api_client.login()

    yield github_api_client

    github_api_client.logout()


@pytest.fixture(scope="session")
def GitHub_UI_App():
    # before test

    browser = CONFIG.get("BROWSER")
    browser = BrowsersProvider.get_driver(browser)

    ui_app = GitHubUI(browser)

    # pass driver(WebDriver) object to test
    yield ui_app

    # after test
    ui_app.close()
