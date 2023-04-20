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
        self.should_be_message_adding_product()
        self.should_be_message_price_basket()

    def should_be_message_adding_product(self):
        message = WebDriverWait(self.browser, self.timeout).until(
            EC.presence_of_element_located(ProductPageLocators.ADDING_MESSAGE)
        )
        message = message.text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == message, "Product name is not in view"

    def should_be_message_price_basket(self):
        message = WebDriverWait(self.browser, self.timeout).until(
            EC.presence_of_element_located(ProductPageLocators.ADDING_TO_BASKET)
        )
        message = message.text
        price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price in message, "Price is not in view"
    