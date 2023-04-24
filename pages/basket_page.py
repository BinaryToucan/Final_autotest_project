from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

EMPTY_TEXT = " Ваша корзина пуста "
class BasketPage(BasePage):

    def __init__(self, browser, url, timeout = 20):
        super().__init__(browser, url)
        self.timeout = timeout

    def should_basket_empty(self):
        if(self.is_not_element_present(*BasketPageLocators.CONTENT_BASKET_EMPTY)):
            assert False, "Basket is not empty"
        message = self.browser.find_element(*BasketPageLocators.CONTENT_BASKET_EMPTY).text
        assert message, f"Text about empty basket is not exist"

    