from selenium import webdriver

from src.config.config import CONFIG



class RemoteEdgeBrowser:
    
    @staticmethod
    def get_driver():
        options = webdriver.EdgeOptions()
        # options.set_capability("pageLoadStrategy", "normal")
        # options.set_capability("platformName", "windows")
        driver = webdriver.Remote(
            command_executor=CONFIG.get("SELENIUM_GRID_URL"),
            options=options
        )

        return driver

