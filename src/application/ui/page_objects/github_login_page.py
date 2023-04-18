from src.application.ui.page_objects.github_base_page import BasePage
from selenium.webdriver.common.by import By



class LoginPageLocators:

    USERNAME_INPUT = (By.ID, 'login_field')
    PASSWORD_INPUT = (By.ID, 'password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    INCORRECT_USERNAME_OR_PASS_ALERT = (By.CSS_SELECTOR, "div[role='alert']")
    TO_MUCH_FAILED_LOGIN = (By.CSS_SELECTOR, "div#login > p")
    PASSWORD_RESET_LINK = (By.LINK_TEXT, "Forgot password?")
    CREATE_AN_ACCOUNT = (By.LINK_TEXT, "Create an account")
    TERMS = (By.LINK_TEXT, "Terms")
    PRIVACY = (By.LINK_TEXT, "Privacy")
    SECURITY = (By.LINK_TEXT, "Security")
    CONTACT_GITHUB = (By.LINK_TEXT, "Contact GitHub")
    

class LoginPage(BasePage):

    URL = "/login"

    def go_to(self):
        self.driver.get(self.base_url + LoginPage.URL)
        return self

    def go_to_signup_page(self):
        self.click(LoginPageLocators.CREATE_AN_ACCOUNT)
        self.wait_until_url_changes(self.base_url + self.URL)
        return self
    
    def go_to_password_reset_page(self):
        self.click(LoginPageLocators.PASSWORD_RESET_LINK)
        self.wait_until_url_changes(self.base_url + self.URL)
        return self
    
    def go_to_terms_page(self):
        self.click(LoginPageLocators.TERMS)
        self.wait_until_url_changes(self.base_url + self.URL)
        return self
    
    def go_to_privacy_page(self):
        self.click(LoginPageLocators.PRIVACY)
        self.wait_until_url_changes(self.base_url + self.URL)
        return self
    
    def go_to_security_page(self):
        self.click(LoginPageLocators.SECURITY)
        self.wait_until_url_changes(self.base_url + self.URL)
        return self
    
    def go_to_github_support_page(self):
        self.click(LoginPageLocators.CONTACT_GITHUB)
        self.wait_until_url_changes(self.base_url + self.URL)
        return self

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

    def get_login_page_title_text(self) -> str:
        text = self.get_title()
        return text
    
    