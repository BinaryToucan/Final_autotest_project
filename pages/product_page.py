from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    def __init__(self, browser, url, timeout = 20):
        super().__init__(browser, url)
        self.timeout = timeout

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()
        super().solve_quiz_and_get_code()

    def is_message_adding_product_exist(self):
        message = WebDriverWait(self.browser, self.timeout).until(
            EC.presence_of_element_located(ProductPageLocators.ADDING_MESSAGE)
        )
        message = message.text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name == message

    def is_message_price_basket_exist(self):
        message = WebDriverWait(self.browser, self.timeout).until(
            EC.presence_of_element_located(ProductPageLocators.ADDING_TO_BASKET)
        )
        message = message.text
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        return price in message
    
    def should_be_message_adding_product_and_price(self):
        assert self.is_message_adding_product_exist() and self.is_message_price_basket_exist()

    def should_be_not_present_message_adding_product(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDING_MESSAGE), "Adding message exist"

    def should_be_disappeared_message_adding_product(self):
        assert self.is_disappeared(*ProductPageLocators.ADDING_MESSAGE), "Adding message not remove after 4 sec"