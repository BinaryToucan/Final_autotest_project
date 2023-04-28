from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

url_part = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
bugged_url_id = 7
urls = [f"{url_part}/?promo=offer{i}" for i in range(10) if i != bugged_url_id]

@pytest.mark.login_guest
class TestGuestFromProductPage():

    @pytest.mark.parametrize('link', urls)
    def test_guest_can_add_product_to_basket(self, browser, link):
        print(f"--- {link} ---")
        page = ProductPage(browser, link)   
        page.open()                      
        page.add_to_basket()
        page.should_be_message_adding_product_and_price()

    @pytest.mark.xfail
    @pytest.mark.parametrize('link', [f"{url_part}/?promo=offer{bugged_url_id}"])
    def test_guest_can_add_product_to_basket_with_bug(self, browser, link):
        print(f"--- {link} ---")
        page = ProductPage(browser, link)   
        page.open()                      
        page.add_to_basket()
        page.should_be_message_adding_product_and_price()

    def test_guest_can_add_product_to_basket_promo_2019(self, browser):
        link = f"{url_part}/?promo=newYear2019"
        page = ProductPage(browser, link)         
        page.open()                      
        page.add_to_basket()
        page.should_be_message_adding_product_and_price()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = f"{url_part}/?promo=newYear2019"
        page = ProductPage(browser, link)         
        page.open()                      
        page.add_to_basket()
        page.should_be_not_present_message_adding_product()

    def test_guest_cant_see_success_message(self, browser):
        link = f"{url_part}/?promo=newYear2019"
        page = ProductPage(browser, link)         
        page.open()          
        page.should_be_not_present_message_adding_product()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = f"{url_part}/?promo=newYear2019"
        page = ProductPage(browser, link)         
        page.open()                      
        page.add_to_basket()
        page.should_be_disappeared_message_adding_product()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = f"{url_part}/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_basket_empty()

@pytest.mark.user_with_product_page
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function")
    def setup(self, broswer):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = f"{url_part}/?promo=newYear2019"
        page = ProductPage(browser, link)         
        page.open()          
        page.should_be_not_present_message_adding_product()
    
    def test_user_can_add_product_to_basket(self, browser):
        link = urls[0]
        page = ProductPage(browser, link)   
        page.open()                      
        page.add_to_basket()
        page.should_be_message_adding_product_and_price()
