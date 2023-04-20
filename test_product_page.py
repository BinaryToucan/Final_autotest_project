from .pages.product_page import ProductPage
import time
import pytest

url_part = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
bugged_url_id = 7
urls = [f"{url_part}/?promo=offer{i}" for i in range(10) if i != bugged_url_id]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    print(f"--- {link} ---")
    page = ProductPage(browser, link)   
    page.open()                      
    page.add_to_basket()
    page.should_be_message_adding_product_and_price()

@pytest.mark.xfail
@pytest.mark.parametrize('link', [f"{url_part}/?promo=offer{bugged_url_id}"])
def test_guest_can_add_product_to_basket_with_bug(browser, link):
    print(f"--- {link} ---")
    page = ProductPage(browser, link)   
    page.open()                      
    page.add_to_basket()
    page.should_be_message_adding_product_and_price()

def test_guest_can_add_product_to_basket_promo_2019(browser):
    link = f"{url_part}/?promo=newYear2019"
    page = ProductPage(browser, link)         
    page.open()                      
    page.add_to_basket()
    page.should_be_message_adding_product_and_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"{url_part}/?promo=newYear2019"
    page = ProductPage(browser, link)         
    page.open()                      
    page.add_to_basket()
    page.should_be_not_present_message_adding_product()

def test_guest_cant_see_success_message(browser):
    link = f"{url_part}/?promo=newYear2019"
    page = ProductPage(browser, link)         
    page.open()          
    page.should_be_not_present_message_adding_product()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"{url_part}/?promo=newYear2019"
    page = ProductPage(browser, link)         
    page.open()                      
    page.add_to_basket()
    page.should_be_disappeared_message_adding_product()
