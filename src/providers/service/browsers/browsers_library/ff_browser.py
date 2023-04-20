from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

from src.config.config import config


class FFBrowser:

    @staticmethod
    def get_driver():
        options = Options()
        options.page_load_strategy = 'normal'
        # options.add_argument("disable-infobars")
        # options.add_argument("start-maximized")
        # options.add_argument("disable-dev-shm-usage")
        # options.add_argument("no-sandbox")
        # options.add_argument("disable-blink-features=AutomationControlled")

        if config.get("DEBUG_MODE") is False:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

        return webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )