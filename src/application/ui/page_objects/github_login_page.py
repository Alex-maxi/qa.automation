from src.application.ui.page_objects.github_base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Locators:

    USERNAME_FIELD = (By.ID, 'login_field')
    PASSWORD_FIELD = (By.ID, 'password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    ASSERT_INCORRECT_USERNAME_OR_PASS = (By.CSS_SELECTOR, "div[role='alert']")
    TO_MUCH_FAILED_LOGIN = (By.CSS_SELECTOR, "div#login > p")


class LoginPage(BasePage):

    def enter_user_name(self, input_data=''):
        username_field = self.element_is_visible(Locators.USERNAME_FIELD)
        username_field.clear()
        username_field.send_keys(input_data)
        return self

    def enter_password(self, input_data=''):
        password_field = self.element_is_visible(Locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(input_data)
        return self

    def press_sign_in_button(self):
        sign_in_button = self.element_is_visible(Locators.SIGN_IN_BUTTON)
        sign_in_button.click()
        return self

    def assertion_fail_check(self):
        fail_assertion = self.element_is_visible(
            Locators.ASSERT_INCORRECT_USERNAME_OR_PASS)
        return fail_assertion.is_displayed()
