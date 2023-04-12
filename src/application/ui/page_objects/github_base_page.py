from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open(self, url):
        self._driver.get(url)

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, timeout: int = 10):
        self._wait_until_element_is_visible(locator, timeout)
        self._find(locator).send_keys(text)

    def _wait_until_element_is_visible(self, locator: tuple, timeout: int = 10):
        return Wait(self._driver, timeout).until(EC.visibility_of_element_located(locator))
        
    def _click(self, locator: tuple, timeout: int = 10):
        self._wait_until_element_is_visible(locator, timeout)
        self._find(locator).click()

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    

    