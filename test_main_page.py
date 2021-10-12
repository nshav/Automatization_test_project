from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
#import pytest

def test_guest_can_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


#def test_guest_can_see_login_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_login_form()
#
#
#def test_guest_can_see_register_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_register_form()

#def test_should_be_login_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_login_form()
#
#def test_should_be_register_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_register_form()

#@pytest.mark.login_guest
#class TestLoginMainPage():
#    def test_guest_can_go_to_login_page(self, browser):
#        link = "http://selenium1py.pythonanywhere.com/"
#        page = MainPage(browser, link)
#        page.open()
#        page.go_to_login_page()
#
#    def test_guest_should_see_login_link(self, browser):
#        link = "http://selenium1py.pythonanywhere.com/"
#        page = MainPage(browser, link)
#        page.open()
#        page.should_be_login_link()