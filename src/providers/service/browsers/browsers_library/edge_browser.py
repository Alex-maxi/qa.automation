from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options

from src.config.config import CONFIG


class EdgeBrowser:

    @staticmethod
    def get_driver():
        options = Options()
        options.page_load_strategy = 'normal'
        options.add_argument("start-maximized")
        # options.add_argument("inprivate")

        if CONFIG.get("DEBUG_MODE") is False:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            

        return webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )