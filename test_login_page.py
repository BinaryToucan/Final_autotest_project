from .pages.login_page import LoginPage

def test_should_be_login_page(browser):
    page = LoginPage(browser)         
    page.open()                      
    page.should_be_login_page()          
