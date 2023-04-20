from .base_page import BasePage
from selenium.webdriver.common.by import By

MAIN_URL = "http://selenium1py.pythonanywhere.com/"

class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser, MAIN_URL)
