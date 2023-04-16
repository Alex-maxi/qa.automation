import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.application.api.github_api_client import GitHubApiClient
from src.application.ui.github_ui_app import GitHubUI
from src.config.config import config

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

@pytest.fixture
def github_api_client():
    github_api_client = GitHubApiClient()
    github_api_client.login(config.get("USERNAME"), config.get("PASSWORD"))

    yield github_api_client

    github_api_client.logout()


@pytest.fixture(scope="session")
def GitHub_UI_App():
    # before test
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()

    ui_app = GitHubUI(driver)

    # pass driver(WebDriver) object to test
    yield ui_app

    # after test
    ui_app.close()
