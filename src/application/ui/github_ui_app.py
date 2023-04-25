from src.application.ui.page_objects.github_login_page import LoginPage
from selenium.webdriver.remote.webdriver import WebDriver
from src.config.config import CONFIG

class GitHubUI:


    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.base_url = CONFIG.get("BASE_URL_UI")
        self.LoginPage = LoginPage(self.driver, self.base_url)
        self.SignupPage = None

    def open(self):
        self.driver.get(self.base_url)
        return self

    def close(self):
        self.driver.quit()