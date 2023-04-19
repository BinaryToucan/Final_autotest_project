from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

MAIN_URL = "http://selenium1py.pythonanywhere.com/"

class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser, MAIN_URL)
    
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

