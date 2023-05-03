from selenium.webdriver.remote.webdriver import WebDriver
from src.application.ui.page_objects.github_login_page import LoginPage
from src.config.config import CONFIG

class GitHubUI:


    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.base_url = CONFIG.get("BASE_URL_UI")
        self.login_page = LoginPage(self.driver, self.base_url)
        self.signup_page = None

    def open(self):
        self.driver.get(self.base_url)
        return self

    def close(self):
        self.driver.quit()