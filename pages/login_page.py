from .base_page import BasePage
from .locators import LoginPageLocators

LOGIN_URL = "https://selenium1py.pythonanywhere.com/accounts/login/"

class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser, LOGIN_URL)
        self.login_name = "login"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert self.login_name in current_url, "Url doesn't have 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"