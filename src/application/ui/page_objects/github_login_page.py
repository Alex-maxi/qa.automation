from src.config.config import config
from src.application.ui.page_objects.github_base_page import BasePage
from selenium.webdriver.common.by import By

base_url = config.get('BASE_URL_UI')


class LoginPageLocators:

    USERNAME_INPUT = (By.ID, 'login_field')
    PASSWORD_INPUT = (By.ID, 'password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    INCORRECT_USERNAME_OR_PASS_ALERT = (By.CSS_SELECTOR, "div[role='alert']")
    TO_MUCH_FAILED_LOGIN = (By.CSS_SELECTOR, "div#login > p")
    PASSWORD_RESET_LINK = (By.CSS_SELECTOR, "[href='\/password_reset']")
    TITLE_TEXT = (By.CSS_SELECTOR, "h1")


class LoginPage(BasePage):

    URL = "/login"

    def go_to(self):
        self._driver.get(base_url + LoginPage.URL)

    def go_to_sign_up_page(self):
        self._driver.get(base_url + LoginPage.URL)
        pass

    def enter_user_name(self, input_data: str):
        self.type(LoginPageLocators.USERNAME_INPUT, input_data)
        return self

    def enter_password(self, input_data: str):
        self.type(LoginPageLocators.PASSWORD_INPUT, input_data)
        return self

    def press_sign_in_button(self):
        self.click(LoginPageLocators.SIGN_IN_BUTTON)
        return self
    
    def try_sign_in(self, name_data: str, passwodr_data: str ):
        self.enter_user_name(name_data)
        self.enter_password(passwodr_data)
        self.press_sign_in_button()
        return self

    def check_fail_login_alert(self) -> bool:
        element = self.is_displayed(LoginPageLocators.INCORRECT_USERNAME_OR_PASS_ALERT)
        return element
    
    def check_forgot_password_link(self) -> bool:
        element = self.is_displayed(LoginPageLocators.PASSWORD_RESET_LINK)
        return element

    def get_title_text(self) -> str:
        text = self.get_text(LoginPageLocators.TITLE_TEXT)
        return text