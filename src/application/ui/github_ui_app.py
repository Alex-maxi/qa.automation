from src.application.ui.page_objects.github_login_page import LoginPage
from src.config.config import config
from selenium.webdriver.remote.webdriver import WebDriver

class GitHubUI:

    BASE_URL = config.get("BASE_URL_UI")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.LoginPage = LoginPage(driver, GitHubUI.BASE_URL)
        self.SignupPage = None

    def open(self):
        self.driver.get(self.BASE_URL)
        return self

    def close(self):
        self.driver.quit()