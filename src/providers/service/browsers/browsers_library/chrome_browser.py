from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from src.config.config import CONFIG


class ChromeBrowser:

    @staticmethod
    def get_driver():
        options = Options()
        options.page_load_strategy = 'normal'
        options.add_argument("disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("disable-dev-shm-usage")
        options.add_argument("no-sandbox")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("disable-blink-features=AutomationControlled")

        if CONFIG.get("DEBUG_MODE") is False:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
