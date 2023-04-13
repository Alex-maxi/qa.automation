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


class LoginPage(BasePage):

    @property
    def _url(self):
        return f'{base_url}/login'

    def _open(self):
        super()._open(self._url)

    def enter_user_name(self, input_data: str):
        super()._type(LoginPageLocators.USERNAME_INPUT, input_data)
        return self

    def enter_password(self, input_data: str):
        super()._type(LoginPageLocators.PASSWORD_INPUT, input_data)
        return self

    def press_sign_in_button(self):
        super()._click(LoginPageLocators.SIGN_IN_BUTTON)
        return self

    def assertion_fail_check(self):
        element = super()._is_displayed(LoginPageLocators.INCORRECT_USERNAME_OR_PASS_ALERT)
        return element
    
    def forgot_password_link_check(self):
        element = super()._is_displayed(LoginPageLocators.PASSWORD_RESET_LINK)
        return element
