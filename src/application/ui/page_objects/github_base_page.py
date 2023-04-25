from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from src.config.config import CONFIG


class BasePage:
        
    def __init__(self, driver: WebDriver, base_url) -> None:
        self.driver = driver
        self.base_url = base_url
        self.base_timeout = CONFIG.get("UI_TIMEOUTS")

    def find(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def type(self, locator: tuple, text: str, timeout: int = None):
        if timeout is None:
            timeout = self.base_timeout
        self.wait_until_element_is_visible(locator, timeout)
        self.find(locator).send_keys(text)

    def wait_until_element_is_visible(self, locator: tuple, timeout: int = None):
        if timeout is None:
            timeout = self.base_timeout
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def get_title(self, timeout: int = None) -> str:
        if timeout is None:
            timeout = self.base_timeout
        Wait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "title")))
        text_title = self.driver.title
        return text_title

    def click(self, locator: tuple, timeout: int = None):
        if timeout is None:
            timeout = self.base_timeout

        self.wait_until_element_is_visible(locator, timeout)
        self.find(locator).click()

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False
        
    def get_text(self, locator: tuple, timeout: int = None) -> str:
        if timeout is None:
            timeout = self.base_timeout
        self.wait_until_element_is_visible(locator, timeout)
        return self.find(locator).text
    
    def get_url(self):
        get_url = self.driver.current_url
        return get_url
    
    def wait_until_url_changes(self, url: str, timeout: int = None):
        if timeout is None:
            timeout = self.base_timeout
        return Wait(self.driver, timeout).until(EC.url_changes(url))

    