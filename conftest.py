import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
def driver():
    # before test
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()

    # pass driver(WebDriver) object to test
    yield driver

    # after test
    driver.quit
