from selenium import webdriver
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_check_login_url(browser):
    login_link = LoginPageLocators.LOGIN_LINK
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_url(browser)

def test_guest_should_see_login_form(browser):
    login_link = LoginPageLocators.LOGIN_LINK
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_form()


def test_guest_should_see_regist_form(browser):
    login_link = LoginPageLocators.LOGIN_LINK
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_register_form()

