from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, "//div[@class='basket-mini pull-right hidden-xs']//a")

class BasketPageLocators():
    CONTENT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.ID, "add_to_basket_form")
    ADDING_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    ADDING_TO_BASKET = (By.XPATH, "//div[@id='messages']/div[3]//strong")
    PRODUCT_NAME = (By.XPATH, "//*[@class='product_page']/div[1]/div[2]/h1")
    PRICE_PRODUCT = (By.XPATH, "//*[@class='product_page']/div[1]/div[2]/p[1]")