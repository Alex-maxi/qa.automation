from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver: WebDriver, base_url) -> None:
        self.driver = driver
        self.base_url = base_url

    def find(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def type(self, locator: tuple, text: str, timeout: int = 10):
        self.wait_until_element_is_visible(locator, timeout)
        self.find(locator).send_keys(text)

    def wait_until_element_is_visible(self, locator: tuple, timeout: int = 10):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def get_title(self, timeout: int = 10) -> str:
        Wait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "title")))
        text_title = self.driver.title
        return text_title

    def click(self, locator: tuple, timeout: int = 10):
        self.wait_until_element_is_visible(locator, timeout)
        self.find(locator).click()

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False
        
    def get_text(self, locator: tuple, timeout: int = 10) -> str:
        self.wait_until_element_is_visible(locator, timeout)
        return self.find(locator).text
    
    def get_url(self):
        get_url = self.driver.current_url
        return get_url
    
    def wait_until_url_changes(self, url: str, timeout: int = 15):
        return Wait(self.driver, timeout).until(EC.url_changes(url))

    